from django.urls import path
from . import views
from .views import FornecedoresList, FornecedorCreate, FornecedorUpdate, FornecedorDelete

app_name = 'fornecedores'  # Isso define o namespace

urlpatterns = [
    path('', FornecedoresList.as_view(), name='fornecedor_list'),
    path('novo/', FornecedorCreate.as_view(), name='fornecedor_create'),
    path('editar/<int:pk>/', FornecedorUpdate.as_view(), name='fornecedor_update'),
    path('excluir/<int:pk>/', FornecedorDelete.as_view(), name='fornecedor_delete'),
]