from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('cadastrar_entrada/', views.cadastrar_entrada, name='cadastrar_entrada'), 

]