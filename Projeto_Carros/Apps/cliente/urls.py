from django.urls import path

from .views import listCliente, CreateCliente, UpdateCliente, ExcluirCliente

urlpatterns = [
    path('clientes/', listCliente.as_view(), name='cliente'),
    path('clientes/adicionar/', CreateCliente.as_view(), name='criar_cliente'),
    path('clientes/atualizar/<pk>/', UpdateCliente.as_view(), name='atualizar_cliente' ),
    path('clientes/excluir/<pk>/', ExcluirCliente.as_view(), name='excluir_cliente' )
]
