from django.urls import path
from . import views

urlpatterns = [
    path('listar_modelos/', views.listar_modelos, name='listar_modelos'),
    path('cadastrar_modelo/', views.cadastrar_modelo, name='cadastrar_modelo'),
    path('editar_modelo/<int:pk>', views.editar_modelo, name='editar_modelo'),
    path('deletar_modelo/<int:pk>', views.deletar_modelo, name='deletar_modelo'),
]
