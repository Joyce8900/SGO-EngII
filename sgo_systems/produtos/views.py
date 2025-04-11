from django.shortcuts import render
from .forms import ProdutoForm
from .models import Produtos

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


def listar_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, "listar_produtos.html", {"produtos": produtos})
