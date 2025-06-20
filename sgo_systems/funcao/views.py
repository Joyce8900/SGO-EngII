from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Funcao
from django.shortcuts import get_object_or_404

# Create your views here.
class CadastrarFuncaoView(View):
    template_name = 'funcao/templates/form_funcao.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        salario = request.POST.get('salario')

        funcao = Funcao(nome=nome, salario=salario)
        funcao.save()

        return redirect('listar_funcoes')
    

class ListarFuncaoView(View):
    template_name = 'funcao/templates/listar_funcao.html'

    def get(self, request, *args, **kwargs):
        filtro_nome = request.GET.get('filtro_nome', '')
        if filtro_nome:
            funcoes = Funcao.objects.filter(nome__icontains=filtro_nome)
        else:
            funcoes = Funcao.objects.all()

        return render(request, self.template_name, {'funcoes': funcoes,})
        

class EditarFuncaoView(View):
    template_name = 'funcao/templates/form_funcao.html'

    def get(self, request, id, *args, **kwargs):
        funcao = get_object_or_404(Funcao, id=kwargs['id'])
        return render(request, self.template_name, {'funcao': funcao})
    
    def post(self, request, id, *args, **kwargs):
        funcao = get_object_or_404(Funcao, id=kwargs['id'])
        funcao.nome = request.POST.get('nome')
        funcao.salario = request.POST.get('salario')
        funcao.save()
        return redirect('listar_funcoes')

class DeletarFuncaoView(View):
    def post(self, request, id, *args, **kwargs):
        funcao = get_object_or_404(Funcao, id=kwargs['id'])
        funcao.delete()
        messages.success(request, "Função deletada com sucesso!")
        return redirect('listar_funcoes')