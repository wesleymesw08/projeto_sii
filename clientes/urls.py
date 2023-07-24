from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('cliente/criar/', views.criar_cliente, name='criar_cliente'),
    path('cliente/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('cliente/excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
]
