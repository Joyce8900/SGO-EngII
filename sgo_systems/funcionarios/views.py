from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .models import Funcionario
from django.shortcuts import get_object_or_404

class CadastrarFuncionarioView(View):
    template_name = 'funcionario/form_funcionario.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        telefone = request.POST.get('telefone')

        if Funcionario.objects.filter(telefone=telefone).exists():
            messages.error(request, "Já existe um funcionário cadastrado com este telefone.")
            return render(request, self.template_name, {'funcionario': {'nome': nome, 'cargo': cargo, 'telefone': telefone}, 'error': 'Telefone já cadastrado.'})
        
        funcionario = Funcionario(nome=nome, cargo=cargo, telefone=telefone)
        funcionario.save()

        return redirect('listar_funcionario')

class ListarFuncionarioView(View):
    template_name = 'funcionario/listar_funcionario.html'

    def get(self, request, *args, **kwargs):
        filtro_nome = request.GET.get('filtro_nome', '')
        if filtro_nome:
            funcionarios = Funcionario.objects.filter(nome__icontains=filtro_nome)
        else:
            funcionarios = Funcionario.objects.all()
        return render(request, self.template_name, {'funcionarios': funcionarios})

class EditarFuncionarioView(View):
    template_name = 'funcionario/form_funcionario.html'

    def get(self, request, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, id=kwargs['pk'])
        return render(request, self.template_name, {'funcionario': funcionario})

    def post(self, request, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, id=kwargs['pk'])
        funcionario.nome = request.POST.get('nome')
        funcionario.cargo = request.POST.get('cargo')
        funcionario.telefone = request.POST.get('telefone')
        funcionario.save()
        return redirect('listar_funcionario')

class DeletarFuncionarioView(View):
    def post(self, request, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, id=kwargs['pk'])
        funcionario.delete()
        messages.success(request, "Funcionário deletado com sucesso!")
        return redirect('listar_funcionario')