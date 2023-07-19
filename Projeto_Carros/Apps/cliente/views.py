from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Cliente
from .form import FormCliente

class listCliente (ListView):
    model = Cliente
    template_name = 'cliente/cliente.html'

class CreateCliente(CreateView):
    model = Cliente
    form_class = FormCliente # form class fica apenas no create...
    template_name = 'form.html'
    success_url = reverse_lazy('cliente')


class UpdateCliente(UpdateView):
    model = Cliente
    template_name = 'form.html'
    success_url = reverse_lazy('cliente')
    fields = '__all__'

class ExcluirCliente(DeleteView):
    model = Cliente
    template_name = 'excluir.html'
    success_url = reverse_lazy('cliente')
    
# Create your views here.
