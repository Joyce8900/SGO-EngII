from django.urls import path
from . import views
from .views import ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete

app_name = 'clientes'

urlpatterns = [
    path('', ClienteList.as_view(), name='cliente_list'),
    path('novo/', ClienteCreate.as_view(), name='cliente_novo'),
    path('editar/<int:pk>/', ClienteUpdate.as_view(), name='cliente_update'),
    path('excluir/<int:pk>/', ClienteDelete.as_view(), name='cliente_delete'),
]
