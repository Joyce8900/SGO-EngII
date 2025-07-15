from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .forms import ProdutoForm, PesquisaProdutoForm
from django.db.models import Q
from .models import Produtos, Categorias
from django.contrib import messages


URL_PRODUTOS = 'produtos:listar_produtos'

class CadastrarProdutos(View):
    template = "cadastrar_produto.html"
    def get(self, request):
        form = ProdutoForm()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(URL_PRODUTOS)
        return render(request, self.template, {"form": form})


class ListarProdutos(View):
    template = "listar_produtos.html"
    def get(self, request):
        form = PesquisaProdutoForm(request.GET or None)
        produtos = Produtos.objects.all().order_by('nome')
        categoria = request.GET.get('categoria')
        termo = request.GET.get('termo')

        if termo:
            produtos = produtos.filter(
                Q(nome__icontains=termo) |
                Q(marca__nome__icontains=termo) |
                Q(fornecedor__nome__icontains=termo)
            )

        if categoria:
            produtos = produtos.filter(categoria=categoria)

        return render(request, self.template, {
            "produtos": produtos,
            "form": form,
        })
    
    def post(self, request):
        return self.get(request)


class EditarProduto(View):
    template = "editar_produto.html"

    def get(self, request, pk):
        produto = get_object_or_404(Produtos, pk=pk)
        form = ProdutoForm(instance=produto)
        return render(request, self.template, {"form": form, "produto": produto})

    def post(self, request, pk):
        produto = get_object_or_404(Produtos, pk=pk)
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto editado com sucesso.")
            return redirect(URL_PRODUTOS)
        return render(request, self.template, {"form": form, "produto": produto})


class ExcluirProduto(View):
    def post(self, request, pk):
        produto = get_object_or_404(Produtos, pk=pk)
        produto.delete()
        messages.success(request, "Produto excluído com sucesso.")
        return redirect(URL_PRODUTOS)
  
    def get(self, request, pk):
        produto = get_object_or_404(Produtos, pk=pk)
        produto.delete()
        return redirect(URL_PRODUTOS)
