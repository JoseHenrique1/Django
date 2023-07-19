from django.urls import path

from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView


urlpatterns = [
    path('', ClienteListView, name='cliente_index'),
    path('ciente/create/', ClienteCreateView, name='cliente_create'),
    path('cliente/update/<int:id>', ClienteUpdateView, name='cliente_update'),
    path('cliente/delete/<int:id>', ClienteDeleteView, name='cliente_delete')
]
