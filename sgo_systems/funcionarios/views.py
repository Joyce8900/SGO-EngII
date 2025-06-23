from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from .models import Funcionario
from funcao.models import Funcao

class CadastrarFuncionarioView(View):
    template_name = 'funcionario/form_funcionario.html'

    def get(self, request, *args, **kwargs):
        funcoes = Funcao.objects.all()
        return render(request, self.template_name, {'funcoes': funcoes})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        funcao_id = request.POST.get('funcao')

        if not funcao_id:
            messages.error(request, "Selecione uma função.")
            funcoes = Funcao.objects.all()
            contexto = {'funcionario': {'nome': nome, 'telefone': telefone}, 'funcoes': funcoes, 'error': 'Selecione uma função.', 'is_edit': False}
            return render(request, self.template_name, contexto)

        funcao = get_object_or_404(Funcao, id=funcao_id)

        if Funcionario.objects.filter(telefone=telefone).exists():
            messages.error(request, "Telefone já cadastrado.")
            funcoes = Funcao.objects.all()
            contexto = {'funcionario': {'nome': nome, 'telefone': telefone}, 'funcoes': funcoes, 'error': 'Telefone já cadastrado.', 'is_edit': False}
            return render(request, self.template_name, contexto)

        funcionario = Funcionario(nome=nome, telefone=telefone, funcao=funcao)
        funcionario.save()

        return redirect('listar_funcionario')

class ListarFuncionarioView(View):
    template_name = 'funcionario/listar_funcionario.html'

    def get(self, request, *args, **kwargs):
        filtro = request.GET.get('filtro', '')
        if filtro:
            funcionarios = Funcionario.objects.filter(Q(nome__icontains=filtro) | Q(telefone__icontains=filtro))
        else:
            funcionarios = Funcionario.objects.all()
        return render(request, self.template_name, {'funcionarios': funcionarios})

class EditarFuncionarioView(View):
    template_name = 'funcionario/form_funcionario.html'

    def get(self, request, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, id=kwargs['pk'])
        funcoes = Funcao.objects.all()
        return render(request, self.template_name, {'funcionario': funcionario, 'funcoes': funcoes, 'is_edit': True})

    def post(self, request, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, id=kwargs['pk'])
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        funcao_id = request.POST.get('funcao')

        if not funcao_id:
            messages.error(request, "Selecione uma função.")
            funcoes = Funcao.objects.all()
            contexto = {'funcionario': {'id': funcionario.id, 'nome': nome, 'telefone': telefone}, 'funcoes': funcoes, 'error': 'Selecione uma função.', 'is_edit': True}
            return render(request, self.template_name, contexto)

        funcao = get_object_or_404(Funcao, id=funcao_id)

        if Funcionario.objects.filter(telefone=telefone).exclude(id=funcionario.id).exists():
            messages.error(request, "Telefone já cadastrado.")
            funcoes = Funcao.objects.all()
            contexto = {'funcionario': {'id': funcionario.id, 'nome': nome, 'telefone': telefone}, 'funcoes': funcoes, 'error': 'Telefone já cadastrado.', 'is_edit': True}
            return render(request, self.template_name, contexto)

        funcionario.nome = nome
        funcionario.telefone = telefone
        funcionario.funcao = funcao
        funcionario.save()

        return redirect('listar_funcionario')

class DeletarFuncionarioView(View):
    def post(self, request, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, id=kwargs['pk'])
        funcionario.delete()
        messages.success(request, "Funcionário deletado com sucesso!")
        return redirect('listar_funcionario')
