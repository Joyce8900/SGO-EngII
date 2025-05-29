from django.db.models import Q
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Entrada
from .forms import EntradaForm
from produtos.models import Produtos
from .forms import PesquisaEntradaForm

class CadastrarEntradaView(View):
    template_name = 'cadastrar_entrada.html'

    def get(self, request):
        form = EntradaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            produto = entrada.produto
            produto.quantidade += entrada.quantidade
            produto.save()
            entrada.save()
            return redirect('listar_entrada')
        return render(request, self.template_name, {'form': form})


class EditarEntradaView(View):
    def post(self, request, pk):
        entrada = get_object_or_404(Entrada, pk=pk)
        produto = entrada.produto
        quantidade_antiga = entrada.quantidade
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            diferenca = nova_entrada.quantidade - quantidade_antiga
            produto.quantidade += diferenca
            produto.preco = nova_entrada.valor
            produto.save()
            nova_entrada.save()
            return redirect("listar_entrada")
        return render(request, "editar_entrada.html", {"form": form})


class ExcluirEntradaView(View):
    def post(self, request, pk):
        entrada = get_object_or_404(Entrada, pk=pk)
        produto = entrada.produto
        produto.quantidade -= entrada.quantidade
        produto.save()
        entrada.delete()
        return redirect("listar_entrada")


class ListarEntradaView(View):
    template_name = 'listar_entrada.html'

    def get(self, request):
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
        return render(request, self.template_name, {
            "entrada": entradas, 
            "form": form,
        })
