from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('', views.listar_funcionario, name='listar_funcionario'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('deletar/<int:id>/', views.excluir_funcionario, name='deletar_funcionario'),
]