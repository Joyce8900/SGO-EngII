from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Fornecedor
from .forms import FornecedorForm, FornecedorFilterForm
from django.db.models import Q
from core.views import LoginRequiredView

URL_FORNECEDORES = 'fornecedores:fornecedor_list'
class FornecedoresList(LoginRequiredView):
    template_name = 'fornecedores/fornecedor_list.html'
    def get(self, request,  *args, **kwargs):
        form_filter = FornecedorFilterForm(request.GET or None)
        fornecedores = Fornecedor.objects.all()
        
        if form_filter.is_valid():
            termo = form_filter.cleaned_data.get('termo')
            if termo:
                fornecedores = fornecedores.filter(
                    Q(nome__icontains=termo) |
                    Q(contato__icontains=termo) |
                    Q(endereco__icontains=termo) 
                )
        
        return render(request, self.template_name, {
            'fornecedores': fornecedores,
            'form_filter': form_filter,
        })
    
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class FornecedorCreate(LoginRequiredView):
    template_name = 'fornecedores/fornecedor_form.html'
    def get(self, request):
        form = FornecedorForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(URL_FORNECEDORES)
        return render(request, self.template_name, {'form': form})

class FornecedorUpdate(LoginRequiredView):
    template_name = 'fornecedores/fornecedor_form.html'
    def get(self, request, pk):
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        form = FornecedorForm(instance=fornecedor)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, pk):
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect(URL_FORNECEDORES)
        return render(request, self.template_name, {'form': form})


class FornecedorDelete(LoginRequiredView):
    def get(self, request, pk):
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        return render(request, 'fornecedores/fornecedor_delete.html', {'fornecedor': fornecedor})
    
    def post(self, request, pk):    
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        fornecedor.delete()
        return redirect(URL_FORNECEDORES)
