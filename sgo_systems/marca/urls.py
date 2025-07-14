from . import views
from django.urls import path


app_name = 'marca'


urlpatterns = [
   path('cadastrar_marca/', views.cadastrar_marca, name='cadastrar_marca'),
   path('', views.listar_marcas, name='listar_marcas'),
   path('deletar_marca/<int:pk>', views.deletar_marca, name='deletar_marca'),
   path('editar_marca/<int:pk>', views.editar_marca, name='editar_marca'),
]
