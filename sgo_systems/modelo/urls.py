from django.urls import path, include
from . import views

urlpatterns = [
  path('cadastrar_modelo/', views.cadastrar_modelo, name='cadastrar_modelo'),
]