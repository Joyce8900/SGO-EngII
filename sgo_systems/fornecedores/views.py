from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Fornecedor
from .forms import FornecedorForm, FornecedorFilterForm

url_fornecedores = 'fornecedores:fornecedor_list'

# class ForncedoresList(View):
#     def get(self):
#         form_filter = ClienteFilterForm(request.GET or None)
#         clientes = Cliente.objects.all()
        
#         if form_filter.is_valid():
#             termo = form_filter.cleaned_data.get('termo')
#             if termo:
#                 clientes = clientes.filter(
#                     Q(nome__icontains=termo) |
#                     Q(cpf__icontains=termo) |
#                     Q(contato__icontains=termo) |
#                     Q(endereco__icontains=termo)
#                 )

def fornecedor_list(request):
    form_filter = FornecedorFilterForm(request.GET or None)
    fornecedores = Fornecedor.objects.all()
    
    if form_filter.is_valid():
        nome = form_filter.cleaned_data.get('nome')
        contato = form_filter.cleaned_data.get('contato')
        
        if nome:
            fornecedores = fornecedores.filter(nome__icontains=nome)
        if contato:
            fornecedores = fornecedores.filter(contato__icontains=contato)
    
    return render(request, 'fornecedores/fornecedor_list.html', {
        'fornecedores': fornecedores,
        'form_filter': form_filter,
    })

def fornecedor_create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(url_fornecedores)
    else:
        form = FornecedorForm()
    
    return render(request, 'fornecedores/fornecedor_form.html', {'form': form})

def fornecedor_update(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect(url_fornecedores)  
    else:
        form = FornecedorForm(instance=fornecedor)
    
    return render(request, 'fornecedores/fornecedor_form.html', {'form': form})

def fornecedor_delete(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    
    if request.method == 'POST':
        fornecedor.delete()
        return redirect(url_fornecedores)  
    
    return render(request, 'fornecedores/fornecedor_delete.html', {'fornecedor': fornecedor})