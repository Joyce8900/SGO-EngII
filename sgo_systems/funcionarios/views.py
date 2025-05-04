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
