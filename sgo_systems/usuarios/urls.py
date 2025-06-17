from django.urls import path
from .views import Cadastro, Login, Plataforma

urlpatterns = [
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('login/', Login.as_view(),name= 'login'),
    path('plataforma/', Plataforma.as_view(), name='plataforma'),

]