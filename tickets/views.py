from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm, CadastroForm # CadastroForm definido abaixo

# --- AUTENTICAÇÃO ---

def signup(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='tickets.backends.EmailBackend')
            return redirect('dashboard')
    else:
        form = CadastroForm()
    return render(request, 'registration/signup.html', {'form': form})

# --- SISTEMA ---

@login_required
def dashboard(request):
    """ Esta é a HOMEPAGE """
    # Filtros visuais simples
    status_filter = request.GET.get('status')
    
    if request.user.is_staff:
        # Técnico vê tudo
        tickets = Ticket.objects.all().order_by('-criado_em')
    else:
        # Cliente vê apenas os seus
        tickets = Ticket.objects.filter(solicitante=request.user).order_by('-criado_em')

    if status_filter:
        tickets = tickets.filter(status=status_filter)

    return render(request, 'tickets/dashboard.html', {'tickets': tickets})

# (Mantenha as views novo_ticket e detalhe_ticket criadas anteriormente)
@login_required
def novo_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.solicitante = request.user
            ticket.save()
            return redirect('dashboard')
    else:
        form = TicketForm()
    return render(request, 'tickets/new_ticket.html', {'form': form})

@login_required
def detalhe_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    
    # Segurança: Cliente não pode ver ticket de outro cliente (a menos que seja staff)
    if not request.user.is_staff and ticket.solicitante != request.user:
        return redirect('dashboard')

    if request.method == 'POST':
        # Lógica SIMPLIFICADA: Apenas atualização de status pelo técnico
        if 'btn_status' in request.POST and request.user.is_staff:
            novo_status = request.POST.get('novo_status')
            ticket.status = novo_status
            ticket.save()
            return redirect('detalhe_ticket', pk=pk)

    # Não precisamos mais passar o 'ComentarioForm' para o template
    return render(request, 'tickets/view_ticket.html', {'ticket': ticket})

# Adicione esta função ao final do arquivo views.py

@login_required
def editar_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    # Segurança: Apenas o dono ou um técnico pode editar
    if not request.user.is_staff and ticket.solicitante != request.user:
        return redirect('detalhe_ticket', pk=pk)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('detalhe_ticket', pk=pk)
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'tickets/edit_ticket.html', {'form': form, 'ticket': ticket})