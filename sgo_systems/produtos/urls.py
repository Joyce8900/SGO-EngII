from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produtos'), 
]