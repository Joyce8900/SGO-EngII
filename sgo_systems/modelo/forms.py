from django import forms
from .models import Modelo

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nome', 'marca']
        labels = {
            'nome': 'Nome do Modelo',
            'marca': 'Marca',
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do modelo'
            }),
            'marca': forms.Select(attrs={
                'class': 'form-control'
            }),
        }