from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CadastrarProdutos, ListarProdutos, EditarProduto, ExcluirProduto

urlpatterns = [
  path('cadastrar_produto/', CadastrarProdutos.as_view(), name='cadastrar_produto'), 
  path('listar_produtos/', ListarProdutos.as_view(), name='listar_produtos'),
  path('editar_produto/<int:pk>', EditarProduto.as_view(), name='editar_produto'),
  path('excluir_produto/<int:pk>', ExcluirProduto.as_view(), name='excluir_produto'),
]