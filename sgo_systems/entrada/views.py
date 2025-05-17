from django.shortcuts import redirect, render
from .forms import EntradaForm
from produtos.models import Produtos

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
            return redirect('cadastrar_entrada')
        else:
            print("Erros do formulário:", form.errors)  # 👈 Veja o que está errado
    else:
        form = EntradaForm()

    return render(request, "cadastrar_entrada.html", {"form": form})
