from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#from django.views.decorators.http import require_GET

@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(View):
    def get(self, request):
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
