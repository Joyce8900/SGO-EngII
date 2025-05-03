from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_funcionario', views.cadastrar_funcionario, name="cadastrar_funcionario")
]