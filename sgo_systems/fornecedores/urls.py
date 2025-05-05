from django.urls import path
from . import views

app_name = 'fornecedores'  # Isso define o namespace

urlpatterns = [
    path('', views.fornecedor_list, name='fornecedor_list'),
    path('novo/', views.fornecedor_create, name='fornecedor_create'),
    path('editar/<int:pk>/', views.fornecedor_update, name='fornecedor_update'),
    path('excluir/<int:pk>/', views.fornecedor_delete, name='fornecedor_delete'),
]