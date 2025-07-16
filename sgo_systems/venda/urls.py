from django.urls import path
from .views import DeletarVendaView, CadastrarVendaView,  VendaView

app_name = 'venda'

urlpatterns = [
    path('', VendaView.as_view(), name='listar_venda'),
    path('cadastrar/', CadastrarVendaView.as_view(), name='cadastrar_venda'),
    # path('editar/<int:pk>/', EditarVendaView.as_view(), name='editar_venda'),
    path('excluir/<int:pk>/', DeletarVendaView.as_view(), name='excluir_venda'),
]
