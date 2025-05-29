from django.urls import path
from .views import CadastrarEntradaView, EditarEntradaView, ExcluirEntradaView, ListarEntradaView

urlpatterns = [
    path('cadastrar/', CadastrarEntradaView.as_view(), name='cadastrar_entrada'),
    path('editar/<int:pk>/', EditarEntradaView.as_view(), name='editar_entrada'),
    path('excluir/<int:pk>/', ExcluirEntradaView.as_view(), name='excluir_entrada'),
    path('listar/', ListarEntradaView.as_view(), name='listar_entrada'),
]
