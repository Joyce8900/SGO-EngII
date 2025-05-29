from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProdutoForm, PesquisaProdutoForm
from django.db.models import Q
from .models import Produtos, Categorias
from django.contrib import messages

def cadastrar_produtos(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✔ Produto cadastrado com sucesso!")
            return redirect("listar_produtos")
    form = ProdutoForm()
    return render(request, "cadastrar_produto.html", {"form": form})


def listar_produtos(request):
    form = PesquisaProdutoForm(request.GET or None)
    produtos = Produtos.objects.all().order_by('nome')
    categoria = request.GET.get('categoria')
    termo = request.GET.get('termo')

    if termo:
        produtos = produtos.filter(
            Q(nome__icontains=termo) |
            Q(marca__nome__icontains=termo) |
            Q(preco__icontains=termo)
        )

    if categoria:
        produtos = produtos.filter(categoria=categoria)

    return render(request, "listar_produtos.html", {
        "produtos": produtos,
        "form": form,
    })


def editar_produto(request, pk):
    produto = Produtos.objects.get(pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("listar_produtos")
    else:
        form = ProdutoForm(instance=produto)
        print(form.errors)

    return render(request, "editar_produto.html", {"form": form})


def excluir_produto(request, pk):
    produto = get_object_or_404(Produtos, pk=pk)
    produto.delete()
    messages.success(request, "Produto deletado com sucesso!")
    return redirect("listar_produtos")
