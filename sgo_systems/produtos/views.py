from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutoForm

def cadastrar_produtos(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
            return render(request, 'cadastrar_produto.html', {'form': form})
    else:
        
        form = ProdutoForm()

    return render(request, "cadastrar_produto.html", {"form": form})


# def cadastrar_produtos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        cor = request.POST.get('cor')
        tamanho = request.POST.get('tamanho')
        marca = request.POST.get('marca')
        descricao = request.POST.get('descricao')
        
        produto = Produtos(
            nome=nome,
            preco=preco,
            quantidade=quantidade,
            cor=cor,
            tamanho=tamanho,
            marca=marca,
            descricao=descricao
        )
        produto.save()
    return render(request, 'cadastrar_produto.html')  