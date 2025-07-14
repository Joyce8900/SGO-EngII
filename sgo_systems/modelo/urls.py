from django.urls import path
from . import views
from .views import CadastrarModelo, ListarModelos, EditarModelo, DeletarModelo


app_name = 'modelo'


urlpatterns = [
    path('', ListarModelos.as_view(), name='listar_modelos'),
    path('cadastrar_modelo/', CadastrarModelo.as_view(), name='cadastrar_modelo'),
    path('editar_modelo/<int:pk>', EditarModelo.as_view(), name='editar_modelo' ),
    path('deletar_modelo/<int:pk>', DeletarModelo.as_view(), name='deletar_modelo' ),
]
