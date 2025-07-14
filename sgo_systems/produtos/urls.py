from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'produtos'

urlpatterns = [
  path('cadastrar_produto/', views.cadastrar_produtos, name='cadastrar_produto'), 
  path('', views.listar_produtos, name='listar_produtos'),
  path('editar_produto/<int:pk>', views.editar_produto, name='editar_produto'),
  path('excluir_produto/<int:pk>', views.excluir_produto, name='excluir_produto'),
  
]