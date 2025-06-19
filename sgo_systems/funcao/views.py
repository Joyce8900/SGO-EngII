from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Funcao
from django.shortcuts import get_object_or_404

# Create your views here.
class CadastrarFuncaoView(View):
    template_name = 'funcao/cadastrar_funcao.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        salario = request.POST.get('salario')

        funcao = Funcao(nome=nome, salario=salario)
        funcao.save()

        return redirect('listar_funcoes')
