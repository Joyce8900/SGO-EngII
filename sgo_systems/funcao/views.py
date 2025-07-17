from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Funcao
from django.shortcuts import get_object_or_404
from django.db.models.deletion import ProtectedError

# Create your views here.
class CadastrarFuncaoView(View):
    template_name = 'funcao/form_funcao.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        salario = request.POST.get('salario')

        funcao = Funcao(nome=nome, salario=salario)
        funcao.save()

        return redirect('funcao:listar_funcoes') # CORRIGIDO AQUI
    

class ListarFuncaoView(View):
    template_name = 'funcao/listar_funcao.html'

    def get(self, request, *args, **kwargs):
        filtro_nome = request.GET.get('filtro_nome', '')
        if filtro_nome:
            funcoes = Funcao.objects.filter(nome__icontains=filtro_nome)
        else:
            funcoes = Funcao.objects.all()

        return render(request, self.template_name, {'funcoes': funcoes,})
        

class EditarFuncaoView(View):
    template_name = 'funcao/form_funcao.html'

    def get(self, request, *args, **kwargs):
        funcao = get_object_or_404(Funcao, id=kwargs['pk'])
        return render(request, self.template_name, {'funcao': funcao})
    
    def post(self, request, *args, **kwargs):
        funcao = get_object_or_404(Funcao, id=kwargs['pk'])
        funcao.nome = request.POST.get('nome')
        funcao.salario = request.POST.get('salario')
        funcao.save()
        return redirect('funcao:listar_funcoes') # CORRIGIDO AQUI

class DeletarFuncaoView(View):
    def post(self, request, *args, **kwargs):
        funcao = get_object_or_404(Funcao, id=kwargs['pk'])
        try:
            funcao.delete()
            messages.success(request, "Função deletada com sucesso!")
        except ProtectedError:
            messages.error(request, "Não é possível deletar esta função porque há funcionários associados a ela.")
        return redirect('funcao:listar_funcoes') # CORRIGIDO AQUI