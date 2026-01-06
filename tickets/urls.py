from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('novo/', views.novo_ticket, name='novo_ticket'),
    path('chamado/<int:pk>/', views.detalhe_ticket, name='detalhe_ticket'),
    path('chamado/<int:pk>/editar/', views.editar_ticket, name='editar_ticket'),
    path('cadastro/', views.signup, name='signup'),
]