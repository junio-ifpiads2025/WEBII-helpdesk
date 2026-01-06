from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('ABERTO', 'Aberto'),
        ('ANDAMENTO', 'Em Andamento'),
        ('FECHADO', 'Concluído'),
    )
    
    PRIORIDADE_CHOICES = (
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Média'),
        ('ALTA', 'Alta'),
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField("Descrição do Problema")
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_abertos')
    tecnico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_atendidos')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTO')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='MEDIA')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} - {self.titulo}"
