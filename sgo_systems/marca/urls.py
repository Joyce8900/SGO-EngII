from django.urls import path
from .views import MarcaList, MarcaCreate, MarcaUpdate, MarcaDelete


app_name = 'marca'


urlpatterns = [
   path('cadastrar_marca/', MarcaCreate.as_view(), name='cadastrar_marca'),
   path('', MarcaList.as_view(), name='listar_marcas'),
   path('deletar_marca/<int:pk>', MarcaDelete.as_view(), name='deletar_marca'),
   path('editar_marca/<int:pk>', MarcaUpdate.as_view(), name='editar_marca'),
]
