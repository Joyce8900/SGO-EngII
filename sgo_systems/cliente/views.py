from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm, ClienteFilterForm

def cliente_list(request):
    form_filter = ClienteFilterForm(request.GET or None)
    clientes = Cliente.objects.all()
    
    if form_filter.is_valid():
        nome = form_filter.cleaned_data.get('nome')
        if nome:
            clientes = clientes.filter(nome__icontains=nome)
    
    return render(request, 'cliente_list.html', {
        'clientes': clientes,
        'form_filter': form_filter,
    })

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:cliente_list')
    else:
        form = ClienteForm()
    
    return render(request, 'cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:cliente_list')
    
    return render(request, 'cliente_delete.html', {'cliente': cliente})
