from django.shortcuts import redirect, render, get_object_or_404
from .forms import EntradaForm, PesquisaEntradaForm
from .models import Entrada
from produtos.models import Produtos
from django.db.models import Q


def cadastrar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            produto = entrada.produto
            print("Antes:", produto.quantidade)
            produto.quantidade += entrada.quantidade
            produto.save()
            entrada.save()
            print("Depois:", produto.quantidade)
            return redirect('listar_entrada')
        else:
            print("Erros do formulário:", form.errors) 
            return render(request, 'cadastrar_entrada.html', {'form': form})
    else:
        form = EntradaForm()
        return render(request, 'cadastrar_entrada.html', {'form': form})


def listar_entrada(request):
    form = PesquisaEntradaForm(request.GET)
    entradas = Entrada.objects.all().order_by('data_entrada')

    if form.is_valid():
        termo = form.cleaned_data.get('termo')
        funcionario = form.cleaned_data.get('funcionario')
        if termo:
            entradas = entradas.filter(
                Q(produto__nome__icontains=termo) | 
                Q(fornecedor__nome__icontains=termo) |
                Q(funcionario__nome__icontains=termo) 
            )
        if funcionario:
            entradas = entradas.filter(funcionario=funcionario)
    return render(request, "listar_entrada.html", {
        "entrada": entradas, 
        "form": form,
    })


def excluir_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    produto = entrada.produto
    produto.quantidade -= entrada.quantidade
    produto.save()
    entrada.delete()
    return redirect("listar_entrada")


def editar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            diferenca = nova_entrada.quantidade - entrada.quantidade
            produto = nova_entrada.produto
            produto.quantidade += diferenca
            produto.save()
            nova_entrada.save()
            return redirect('listar_entrada')
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'editar_entrada.html', {'form': form})
