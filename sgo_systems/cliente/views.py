from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm, ClienteFilterForm
from django.views import View
from django.db.models import Q
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

CLIENTE_LIST_REDIRECT = 'clientes:cliente_list'
CLIENTE_CREATE_RENDER = 'cliente_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')

class ClienteList(View):
    def get(self, request, *args, **kwargs):
        form_filter = ClienteFilterForm(request.GET or None)
        clientes = Cliente.objects.all()
        
        if form_filter.is_valid():
            termo = form_filter.cleaned_data.get('termo')
            if termo:
                clientes = clientes.filter(
                    Q(nome__icontains=termo) |
                    Q(cpf__icontains=termo) |
                    Q(contato__icontains=termo) |
                    Q(endereco__icontains=termo)
                )
        
        return render(request, 'cliente_list.html', {
            'clientes': clientes,
            'form_filter': form_filter,
        })
    
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

@method_decorator(login_required(login_url='login'), name='dispatch')
   
class ClienteCreate(View):  
    
    def get(self, request):
        return render(request, CLIENTE_CREATE_RENDER, {'form': ClienteForm()})
    
    def post(self, request):

        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(CLIENTE_LIST_REDIRECT)
        return render(request, CLIENTE_CREATE_RENDER, {'form': form})

class ClienteUpdate(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        form = ClienteForm(instance=cliente)
        return render(request, 'cliente_form.html', {'form': form})
    
    def post(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect(CLIENTE_LIST_REDIRECT)
        return render(request, CLIENTE_CREATE_RENDER, {'form': form})


class ClienteDelete(View):
    def get (self, request, pk):
        return render(request, 'cliente_delete.html', {'cliente': get_object_or_404(Cliente, pk=pk)})
    
    def post(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.delete()
        return redirect(CLIENTE_LIST_REDIRECT)
