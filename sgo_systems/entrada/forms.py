from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('quantidade', 'valor', 'produto', 'fornecedor', 'funcionario')
        labels = {
            
            'quantidade': 'Quantidade',
            'valor': 'Valor',
            'produto': 'Produto',
            'fornecedor': 'Fornecedor',
            'funcionario': 'Funcionário',
        }
        widgets = {
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
        }
