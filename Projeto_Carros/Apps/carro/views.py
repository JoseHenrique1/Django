from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Carro
from .form import FormCarro

class listCarro(ListView):
    
    model = Carro
    template_name  = 'carro/index.html'


class CreateCarro(CreateView):
    model=Carro
    template_name  = 'form.html'
    form_class = FormCarro
    success_url = reverse_lazy('index')



class UpdateCarro(UpdateView):
    model = Carro 
    template_name  = 'detail.html'
    success_url = reverse_lazy('index')
    fields = '__all__'   

class ExcluirCarro(DeleteView):
    model = Carro
    template_name = 'excluir.html'
    success_url = reverse_lazy('index')

# Create your views here.
