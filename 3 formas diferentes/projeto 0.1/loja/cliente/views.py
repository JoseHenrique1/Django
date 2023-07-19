from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .form import ClienteForm
# Create your views here.

def ClienteListView(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('pesquisa')
        clientes = Cliente.objects.filter(nome=nome)
    return render(request, 'cliente/index.html', {'clientes': clientes})

def ClienteCreateView(request):
    form = ClienteForm
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        Cliente.objects.create(nome=nome, idade=idade)
        return redirect('cliente_index')
    return render(request, 'form.html', {'form': form})

def ClienteUpdateView(request, id):
    
    #cliente = Cliente.objects.get(pk=id)
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.idade = request.POST.get('idade')
        cliente.save()
        return redirect('cliente_index')
    
    return render(request, 'form.html', {'form': form})


def ClienteDeleteView(request, id):
    cliente = Cliente.objects.filter(pk=id)
    cliente.delete()
    return redirect('cliente_index')