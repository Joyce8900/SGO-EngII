from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produtos

def cadastrar_produtos(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
            return redirect("listar_produtos")
    else:
        form = ProdutoForm()

    return render(request, "cadastrar_produto.html", {"form": form})


def listar_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, "listar_produtos.html", {"produtos": produtos})

def editar_produto(request, pk):
    produto = Produtos.objects.get(pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("listar_produtos")
    else:
        form = ProdutoForm(instance=produto)

    return render(request, "editar_produto.html", {"form": form})


