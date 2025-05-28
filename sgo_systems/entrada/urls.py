from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('cadastrar_entrada/', views.cadastrar_entrada, name='cadastrar_entrada'), 
  path('listar_entrada/', views.listar_entrada, name='listar_entrada'),
  path('excluir_entrada/<int:pk>/', views.excluir_entrada, name='excluir_entrada'),
  path('editar_entrada/<int:pk>/', views.editar_entrada, name='editar_entrada'),

]