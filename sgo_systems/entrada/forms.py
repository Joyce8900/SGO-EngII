from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('data_entrada', 'quantidade', 'valor', 'produto', 'fornecedor', 'funcionario')
        labels = {
            'data_entrada': 'Data da Entrada',
            'quantidade': 'Quantidade',
            'valor': 'Valor',
            'produto': 'Produto',
            'fornecedor': 'Fornecedor',
            'funcionario': 'Funcionário',
        }
        widgets = {
            'data_entrada': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
        }
