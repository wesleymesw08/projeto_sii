from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes
from .forms import ClientesForm

def lista_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClientesForm()
    return render(request, 'criar_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClientesForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form})

def excluir_cliente(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'excluir_cliente.html', {'cliente': cliente})
