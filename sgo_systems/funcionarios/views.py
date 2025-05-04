from django.shortcuts import render, redirect
from .models import Funcionario

# Create your views here.


def cadastrar_funcionario(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_funcionario.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        telefone = request.POST.get('telefone')

        funcionario = Funcionario(
            nome=nome,
            cargo=cargo,
            telefone=telefone,
        )

        funcionario.save()

        return redirect('cadastrar_funcionario')


def listar_funcionario(request):
    # A variável filtro nome irá receber o valor do parametro "filtro_nome" que está dentro do dicionário request.GET, se não encontrar, retorna uma string vazia ''erro.
    filtro_nome = request.GET.get('filtro_nome', '')
    if filtro_nome:
        funcionarios = Funcionario.objects.filter(nome__icontains=filtro_nome)
    else:
        funcionarios = Funcionario.objects.all()
    return render(request, 'listar_funcionario.html', {'funcionarios': funcionarios})
