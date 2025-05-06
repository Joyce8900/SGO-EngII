from . import views
from django.urls import path

urlpatterns = [
   path('cadastrar_marca/', views.cadastrar_marca, name='cadastrar_marca'),
   path('listar_marcas/', views.listar_marcas, name='listar_marcas'),
]
