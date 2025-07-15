from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import Venda
from .forms import VendaForm

URL = '/venda/'

class VendaView(ListView):
    model = Venda
    template_name = 'venda/listar_venda.html'  # Nome correto do template
    context_object_name = 'vendas'

class CadastrarVendaView(CreateView):
    model = Venda
    form_class = VendaForm
    template_name = 'venda/cadastrar_venda.html'
    success_url = URL



class DeletarVendaView(DeleteView):
    model = Venda
    template_name = 'venda/deletar_venda.html'
    success_url = URL
