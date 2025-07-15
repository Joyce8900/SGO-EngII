from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('cadastrar_produto/', views.CadastrarProdutos.as_view(), name='cadastrar_produto'),
    path('listar_produtos/', views.ListarProdutos.as_view(), name='listar_produtos'),
    path('editar_produto/<int:pk>/', views.EditarProduto.as_view(), name='editar_produto'),
    path('excluir_produto/<int:pk>/', views.ExcluirProduto.as_view(), name='excluir_produto'),
]
