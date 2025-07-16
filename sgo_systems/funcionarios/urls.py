# funcionarios/urls.py
from django.urls import path
from .views import (
    CadastrarFuncionarioView,
    ListarFuncionarioView,
    EditarFuncionarioView,
    DeletarFuncionarioView # Importar a nova view
)

app_name = 'funcionarios'

urlpatterns = [
    path('', ListarFuncionarioView.as_view(), name='listar_funcionario'),
    path('cadastrar/', CadastrarFuncionarioView.as_view(), name='cadastrar_funcionario'),
    path('editar/<int:pk>/', EditarFuncionarioView.as_view(), name='editar_funcionario'),
    path('deletar/<int:pk>/', DeletarFuncionarioView.as_view(), name='deletar_funcionario'), # Adicionar esta linha
]