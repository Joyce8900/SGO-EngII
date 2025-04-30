from django import forms
from .models import Modelo

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = (['nome', 'marca'])
        labels = {
            'nome': 'Nome do Modelo',
            'marca': 'Marca',
        }
