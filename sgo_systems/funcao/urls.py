from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_funcao/', views.CadastrarFuncaoView.as_view(), name='cadastrar_funcao'),
    path('', views.ListarFuncaoView.as_view(), name='listar_funcoes'),
    path('editar/<int:pk>/', views.EditarFuncaoView.as_view(), name='editar_funcao'),
    path('deletar/<int:pk>/', views.DeletarFuncaoView.as_view(), name='deletar_funcao'),
]
