# vendas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q # Import Q for complex lookups

from .models import Venda
from .forms import VendaForm

class VendaCreateView(CreateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/cadastrar_venda.html'
    success_url = reverse_lazy('venda:listar_vendas')

    def form_valid(self, form):
        messages.success(self.request, '✔ Venda cadastrada com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrar Venda'
        return context

class VendaListView(ListView):
    model = Venda
    template_name = 'vendas/listar_venda.html'
    context_object_name = 'vendas'
    ordering = ['-data']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q') # Get the search query from the URL parameter 'q'

        if query:
            # Filter sales based on client name, funcionario name, or produto name
            queryset = queryset.filter(
                Q(cliente__nome__icontains=query) | # Case-insensitive search in client name
                Q(funcionario__nome__icontains=query) | # Case-insensitive search in funcionario name
                Q(produto__nome__icontains=query) | # Case-insensitive search in product name
                Q(valor_total__icontains=query) # Allow searching by part of the total value (if numeric search is desired)
            ).distinct() # Use distinct() to avoid duplicate results if a sale matches multiple conditions

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '') # Pass the current query back to the template for display
        return context

class VendaUpdateView(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/cadastrar_venda.html'
    success_url = reverse_lazy('venda:listar_vendas')

    def form_valid(self, form):
        messages.success(self.request, '✔ Venda editada com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Venda'
        return context

class VendaDeleteView(DeleteView):
    model = Venda
    template_name = 'vendas/deletar_venda.html'
    success_url = reverse_lazy('venda:listar_vendas')
    context_object_name = 'venda'

    def form_valid(self, form):
        messages.success(self.request, '✔ Venda excluída com sucesso!')
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, '✔ Venda excluída com sucesso!')
        return super().post(request, *args, **kwargs)