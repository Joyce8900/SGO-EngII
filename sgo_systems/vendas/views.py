# vendas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.db import transaction
from .models import Venda, ItemVenda
from .forms import VendaForm, ItemVendaFormSet 
from produtos.models import Produtos
from django.utils import timezone

URL_VENDAS = 'venda:listar_vendas'

class VendaCreateView(CreateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/cadastrar_venda.html'
    success_url = reverse_lazy(URL_VENDAS) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            print("=== POST Data ===")
            for key, value in self.request.POST.items():
                print(f"{key}: {value}")
            context['formset'] = ItemVendaFormSet(self.request.POST)
        else:
            context['formset'] = ItemVendaFormSet()
        
        # Adiciona lista de produtos para o select
        context['produtos'] = Produtos.objects.select_related('categoria').all()
        context['title'] = 'Cadastrar Venda'
        return context

    @transaction.atomic
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Debug - veja o que está vindo no POST
        print("POST data:", self.request.POST)
        print("Formset é válido?", formset.is_valid())
        print("Formset errors:", formset.errors)

        if formset.is_valid():
            # Salva a venda
            self.object = form.save(commit=False)
            self.object.valor_total = 0
            self.object.save()

            # Salva os itens vinculando à venda
            formset.instance = self.object
            itens = formset.save(commit=False)
            
            print("Quantidade de itens:", len(itens))
            
            if not itens:
                messages.error(self.request, '❌ Adicione pelo menos um produto ao carrinho!')
                self.object.delete()
                return self.form_invalid(form)
            
            valor_total = 0
            for item in itens:
                # Verifica estoque (se seu modelo tiver esse campo)
                if hasattr(item.produto, 'estoque') and item.produto.estoque < item.quantidade:
                    messages.error(
                        self.request, 
                        f'❌ Estoque insuficiente para {item.produto.nome}. Disponível: {item.produto.estoque}'
                    )
                    self.object.delete()
                    return self.form_invalid(form)
                
                item.venda = self.object  # Garante que o item está vinculado à venda
                item.save()
                valor_total += item.produto.preco * item.quantidade
                
                # Atualiza estoque (se aplicável)
                if hasattr(item.produto, 'estoque'):
                    item.produto.estoque -= item.quantidade
                    item.produto.save()

            self.object.valor_total = valor_total
            self.object.save()

            messages.success(
                self.request, 
                f'✅ Venda #{self.object.pk} cadastrada com sucesso! Total: R$ {valor_total:.2f}'
            )
            return redirect(self.success_url)
        else:
            messages.error(self.request, '❌ Erro ao processar a venda. Verifique os dados.')
            print("Formset errors detalhado:", formset.errors)
            return self.form_invalid(form)


class VendaListView(ListView):
    model = Venda
    template_name = 'vendas/listar_venda.html'
    context_object_name = 'vendas'
    ordering = ['-data']
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset().select_related('cliente', 'funcionario')
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(cliente__nome__icontains=query) |
                Q(funcionario__nome__icontains=query) |
                Q(itens_venda__produto__nome__icontains=query) |
                Q(valor_total__icontains=query)
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context



# Adicione esta view no seu views.py

from django.views.generic import DetailView
from django.db.models import Sum

class VendaDetailView(DetailView):
    model = Venda
    template_name = 'vendas/detalhe_venda.html'
    context_object_name = 'venda'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pega todos os itens relacionados à venda
        itens = self.object.itens_venda.select_related('produto', 'produto__categoria').all()
        context['itens'] = itens
        
        # Calcula a quantidade total de produtos
        quantidade_total = self.object.itens_venda.aggregate(
            total=Sum('quantidade')
        )['total'] or 0
        
        context['quantidade_total'] = quantidade_total
        
        print(f"=== DEBUG ===")
        print(f"Tipos de itens: {itens.count()}")
        print(f"Quantidade total: {quantidade_total}")
        
        return context
    

class VendaUpdateView(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/cadastrar_venda.html'
    success_url = reverse_lazy(URL_VENDAS)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ItemVendaFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = ItemVendaFormSet(instance=self.object)
        
        context['produtos'] = Produtos.objects.select_related('categoria').all()
        context['title'] = 'Editar Venda'
        return context

    @transaction.atomic
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            # Restaura estoque dos itens antigos (se aplicável)
            itens_antigos = ItemVenda.objects.filter(venda=self.object)
            for item in itens_antigos:
                if hasattr(item.produto, 'estoque'):
                    item.produto.estoque += item.quantidade
                    item.produto.save()

            # Salva a venda atualizada
            self.object = form.save(commit=False)
            self.object.valor_total = 0
            self.object.save()

            # Deleta itens antigos
            itens_antigos.delete()

            # Salva novos itens
            formset.instance = self.object
            itens = formset.save(commit=False)
            
            valor_total = 0
            for item in itens:
                # Verifica estoque
                if hasattr(item.produto, 'estoque') and item.produto.estoque < item.quantidade:
                    messages.error(
                        self.request, 
                        f'❌ Estoque insuficiente para {item.produto.nome}'
                    )
                    return self.form_invalid(form)
                
                item.save()
                valor_total += item.produto.preco * item.quantidade
                
                # Atualiza estoque
                if hasattr(item.produto, 'estoque'):
                    item.produto.estoque -= item.quantidade
                    item.produto.save()

            self.object.valor_total = valor_total
            self.object.save()

            messages.success(self.request, '✅ Venda editada com sucesso!')
            return redirect(self.success_url)
        else:
            messages.error(self.request, '❌ Erro ao editar a venda.')
            return self.form_invalid(form)


class VendaDeleteView(DeleteView):
    model = Venda
    template_name = 'vendas/deletar_venda.html'
    success_url = reverse_lazy(URL_VENDAS)
    context_object_name = 'venda'

    @transaction.atomic
    def form_valid(self, form):
        # Restaura estoque antes de deletar (se aplicável)
        itens = ItemVenda.objects.filter(venda=self.object)
        for item in itens:
            if hasattr(item.produto, 'estoque'):
                item.produto.estoque += item.quantidade
                item.produto.save()
        
        messages.success(self.request, '✅ Venda excluída com sucesso!')
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)