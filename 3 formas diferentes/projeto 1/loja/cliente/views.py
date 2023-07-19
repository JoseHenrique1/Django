from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente

def ClienteListView(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/index.html',{ 'clientes': clientes}) 


def ClienteCreateView(request):
    form = ClienteForm()
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)# pega todos os dados
        form.save()
        return redirect('cliente_index')
    return render(request, 'form.html', {'form': form})
    
  
def ClienteUpdateView(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        form.save()
        return redirect('cliente_index')
        
    return render(request, 'form.html', {'form': form})

def ClienteDeleteView(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect('cliente_index')  