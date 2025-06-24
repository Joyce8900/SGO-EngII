from django import forms
from .models import Marca

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']
        labels = {
            'nome': 'Nome da Marca',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
