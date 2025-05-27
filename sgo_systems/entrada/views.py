from django.shortcuts import redirect, render
from .forms import EntradaForm
from .models import Entrada
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from .models import Entrada
from .forms import PesquisaEntradaForm
from produtos.models import Produtos
from django.shortcuts import get_object_or_404

@require_http_methods(['GET',"POST"])
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

   

@require_http_methods(["GET"])
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


@require_http_methods(["GET", "POST"])
def excluir_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    entrada.delete()
    return redirect("listar_entrada")


@require_http_methods(["GET", "POST"])
def editar_entrada(request, pk):
    entrada = Entrada.objects.get(pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            produto = Produtos.objects.get(id=entrada.produto.id)
            produto.quantidade = form.cleaned_data['quantidade']
            produto.preco = form.cleaned_data['valor']
            produto.save()
            return redirect('listar_entrada')
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'editar_entrada.html', {'form': form})