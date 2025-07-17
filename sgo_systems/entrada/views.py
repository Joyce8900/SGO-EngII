from django.db.models import Q
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Entrada, Produtos
from .forms import EntradaForm, PesquisaEntradaForm
from django.contrib import messages

URL_ENTRADA = 'entrada:listar_entrada'

class CadastrarEntradaView(View):
    template_name = 'cadastrar_entrada.html' # CORRIGIDO AQUI (removido 'entrada/')

    def get(self, request):
        form = EntradaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            produto = entrada.produto
            
            nova_quantidade_produto = produto.quantidade + entrada.quantidade
            if nova_quantidade_produto < 1:
                messages.error(request, "A quantidade resultante para o produto seria inválida.")
                return render(request, self.template_name, {'form': form})
            
            produto.quantidade = nova_quantidade_produto
            produto.save()
            entrada.save()
            messages.success(request, "Entrada cadastrada e estoque atualizado com sucesso!")
            return redirect(URL_ENTRADA)
        
        messages.error(request, "Ocorreu um erro ao cadastrar a entrada. Verifique os dados.")
        return render(request, self.template_name, {'form': form})


class EditarEntradaView(View):
    template_name = "editar_entrada.html" # CORRIGIDO AQUI (removido 'entrada/')

    def get(self, request, pk):
        entrada = get_object_or_404(Entrada, pk=pk)
        form = EntradaForm(instance=entrada)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        entrada_original = get_object_or_404(Entrada, pk=pk)
        quantidade_antiga = entrada_original.quantidade
        produto_original = entrada_original.produto

        form = EntradaForm(request.POST, instance=entrada_original)

        if form.is_valid():
            nova_entrada = form.save(commit=False)
            produto_atualizado = nova_entrada.produto

            if produto_original.pk != produto_atualizado.pk:
                nova_quantidade_original_produto = produto_original.quantidade - quantidade_antiga
                if nova_quantidade_original_produto < 1:
                    messages.error(request, f"Não é possível subtrair {quantidade_antiga} do produto '{produto_original.nome}'. A quantidade resultante seria inválida.")
                    return render(request, self.template_name, {"form": form})
                produto_original.quantidade = nova_quantidade_original_produto
                produto_original.save()

                nova_quantidade_atualizado_produto = produto_atualizado.quantidade + nova_entrada.quantidade
                if nova_quantidade_atualizado_produto < 1:
                    messages.error(request, f"Não é possível adicionar {nova_entrada.quantidade} ao produto '{produto_atualizado.nome}'. A quantidade resultante seria inválida.")
                    return render(request, self.template_name, {"form": form})
                produto_atualizado.quantidade = nova_quantidade_atualizado_produto
            else:
                diferenca = nova_entrada.quantidade - quantidade_antiga
                nova_quantidade_atualizado_produto = produto_atualizado.quantidade + diferenca
                if nova_quantidade_atualizado_produto < 1:
                    messages.error(request, f"A alteração da quantidade do produto '{produto_atualizado.nome}' resultaria em um valor inválido no estoque.")
                    return render(request, self.template_name, {"form": form})
                produto_atualizado.quantidade = nova_quantidade_atualizado_produto
            
            produto_atualizado.save()

            nova_entrada.save()

            messages.success(request, "Entrada atualizada e estoque reajustado com sucesso!")
            return redirect(URL_ENTRADA)
        
        messages.error(request, "Ocorreu um erro ao editar a entrada. Verifique os dados.")
        return render(request, self.template_name, {"form": form})


class ExcluirEntradaView(View):
    def post(self, request, pk):
        entrada = get_object_or_404(Entrada, pk=pk)
        
        produto = entrada.produto
        
        nova_quantidade_produto = produto.quantidade - entrada.quantidade
        if nova_quantidade_produto < 1:
            messages.error(request, f"Não é possível excluir esta entrada. A quantidade do produto '{produto.nome}' no estoque ficaria inválida.")
            return redirect(URL_ENTRADA)
        
        produto.quantidade = nova_quantidade_produto
        produto.save()

        entrada.delete()
        messages.success(request, "Entrada excluída e estoque ajustado com sucesso!")
        return redirect(URL_ENTRADA)

    def get(self, request, pk):
        messages.warning(request, "A exclusão de entradas deve ser feita via POST. Use o botão de exclusão na lista.")
        return redirect(URL_ENTRADA)


class ListarEntradaView(View):
    template_name = 'listar_entrada.html' # CORRIGIDO AQUI (removido 'entrada/')

    def get(self, request):
        form = PesquisaEntradaForm(request.GET or None)
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
            "entradas": entradas,
            "form": form,
        })