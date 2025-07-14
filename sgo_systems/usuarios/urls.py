from django.urls import path
from .views import Cadastro, Login, Home# Mude de Plataforma para Home

urlpatterns = [
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('', Login.as_view(), name='login'),
    path('home/', Home.as_view(), name='home'),  # Atualize esta linha também
   # path('cliente/', Cliente.as_view(), name='cliente'),
]