from django.urls import path
from . import views


app_name = 'funcionarios'


urlpatterns = [
    path('cadastrar_funcionario/', views.CadastrarFuncionarioView.as_view(), name='cadastrar_funcionario'),
    path('', views.ListarFuncionarioView.as_view(), name='listar_funcionario'),
    path('editar/<int:pk>/', views.EditarFuncionarioView.as_view(), name='editar_funcionario'),
    path('deletar/<int:pk>/', views.DeletarFuncionarioView.as_view(), name='deletar_funcionario'),
]

