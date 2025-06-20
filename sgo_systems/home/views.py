from django.shortcuts import render
from django.views.decorators.http import require_GET

@require_GET  # Restringe apenas a GET
def home_view(request):
    modules = [
        {'name': 'Fornecedores', 'url': 'fornecedores/'},
        {'name': 'Produtos', 'url': 'produtos/listar_produtos/'},
        {'name': 'Modelos', 'url': 'modelo/listar_modelos/'},
        {'name': 'Marcas', 'url': 'marca/listar_marcas/'},
        {'name': 'Funcionários', 'url': 'funcionarios/'},
        {'name': 'Clientes', 'url': 'clientes/'},
        {'name': 'Entradas', 'url': 'entrada/listar/'},
    ]
    return render(request, 'home/home.html', {'modules': modules})