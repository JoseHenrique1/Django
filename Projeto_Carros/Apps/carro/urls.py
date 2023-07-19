from django.urls import path

from .views import listCarro, CreateCarro, UpdateCarro, ExcluirCarro

urlpatterns = [
    path('', listCarro.as_view(), name='index'),
    path('criar/', CreateCarro.as_view(), name='criar_carro'),
    path('atualizar/<pk>/', UpdateCarro.as_view(), name='atualizar_carro'),
    path('excluir/<pk>/', ExcluirCarro.as_view(), name='excluir_carro'),
]
