from django.shortcuts import redirect, render
from .forms import EntradaForm
from .models import Entrada
from produtos.models import Produtos
from django.views.decorators.http import require_http_methods

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
            return redirect('cadastrar_entrada')
        else:
            print("Erros do formulário:", form.errors) 
    else:
        form = EntradaForm()

    return render(request, 'cadastrar_entrada.html', {'form': form})

@require_http_methods(["GET"])
def listar_entrada(request):
    entrada = Entrada.objects.all().order_by('data_entrada')
    return render(request, "listar_entrada.html", {"entrada": entrada})
    
@require_http_methods(["GET"])
def excluir_entrada(request, pk):
    entrada = Entrada.objects.get(pk=pk)
    entrada.delete()
    return redirect("listar_entrada")