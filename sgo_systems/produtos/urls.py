from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CadastrarProdutos

urlpatterns = [
  path('cadastrar_produto/', CadastrarProdutos.as_view(), name='cadastrar_produto'), 
  path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
  path('editar_produto/<int:pk>', views.editar_produto, name='editar_produto'),
  path('excluir_produto/<int:pk>', views.excluir_produto, name='excluir_produto'),
  
]