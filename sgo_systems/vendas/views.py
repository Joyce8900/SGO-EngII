from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Venda
from .forms import VendaForm

URL_LISTAR_VENDAS = 'venda:listar_vendas' 

class VendaCreateView(CreateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/cadastrar_venda.html'
    success_url = reverse_lazy(URL_LISTAR_VENDAS) # <--- USANDO A CONSTANTE

    def form_valid(self, form):
        messages.success(self.request, '✔ Venda cadastrada com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrar Venda'
        return context

class VendaUpdateView(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/cadastrar_venda.html'
    success_url = reverse_lazy(URL_LISTAR_VENDAS) # <--- USANDO A CONSTANTE

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
    success_url = reverse_lazy(URL_LISTAR_VENDAS) # <--- USANDO A CONSTANTE
    context_object_name = 'venda'

    def form_valid(self, form):
        messages.success(self.request, '✔ Venda excluída com sucesso!')
        return super().form_valid(form)