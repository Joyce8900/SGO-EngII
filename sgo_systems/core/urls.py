from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', include(('home.urls', 'home'), namespace='home')),
    path('fornecedores/', include(('fornecedores.urls', 'fornecedores'), namespace='fornecedores')),
    path('admin/', admin.site.urls),
    path('produtos/', include(('produtos.urls', 'produtos'), namespace='produtos')),
    path('categorias/', include('categorias.urls')),  # Não tem namespace, então não precisa
    path('', include('usuarios.urls')),  # Não tem namespace, então não precisa
    path('modelo/', include(('modelo.urls', 'modelo'), namespace='modelo')),
    path('marca/', include(('marca.urls', 'marca'), namespace='marca')),
    path('funcionarios/', include(('funcionarios.urls', 'funcionarios'), namespace='funcionarios')),
    path('clientes/', include(('cliente.urls', 'clientes'), namespace='clientes')),
    path('entrada/', include(('entrada.urls', 'entrada'), namespace='entrada')),
    path('funcao/', include(('funcao.urls', 'funcao'), namespace='funcao')),
    path('venda/', include('vendas.urls')),
]