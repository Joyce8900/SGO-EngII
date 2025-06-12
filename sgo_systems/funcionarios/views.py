from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Funcionario
from django.shortcuts import get_object_or_404


def cadastrar_funcionario(request):
    if request.method == 'GET':
        return render(request, 'form_funcionario.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        telefone = request.POST.get('telefone')
        
        funcionario = Funcionario(nome=nome, cargo=cargo, telefone=telefone)
        funcionario.save()

        return redirect('listar_funcionario')


def listar_funcionario(request):
    filtro_nome = request.GET.get('filtro_nome', '')
    if filtro_nome:
        funcionarios = Funcionario.objects.filter(nome__icontains=filtro_nome)
    else:
        funcionarios = Funcionario.objects.all()
    return render(request, 'listar_funcionario.html', {'funcionarios': funcionarios})


def editar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'form_funcionario.html', {'funcionario': funcionario})
    elif request.method == 'POST':
        funcionario.nome = request.POST.get('nome')
        funcionario.cargo = request.POST.get('cargo')
        funcionario.telefone = request.POST.get('telefone')
        funcionario.save()
        return redirect('listar_funcionario')


def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    messages.success(request, "Produto deletado com sucesso!")
    return redirect('listar_funcionario')