from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('categorias/', include('categorias.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('modelo/', include('modelo.urls')),
    path('marca/', include('marca.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('clientes/', include('cliente.urls')),
    path('entrada/', include('entrada.urls')),
    path('funcao/', include('funcao.urls')),
    path('venda/', include('venda.urls')),
]