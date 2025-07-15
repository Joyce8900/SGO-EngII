# vendas/urls.py
from django.urls import path
from .views import VendaCreateView, VendaListView, VendaUpdateView, VendaDeleteView

app_name = 'venda'

urlpatterns = [
    path('', VendaListView.as_view(), name='listar_vendas'),
    path('cadastrar/', VendaCreateView.as_view(), name='cadastrar_venda'),
    path('editar/<int:pk>/', VendaUpdateView.as_view(), name='editar_venda'),
    path('deletar/<int:pk>/', VendaDeleteView.as_view(), name='deletar_venda'),
]