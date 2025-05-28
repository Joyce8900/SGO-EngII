from django import forms
from .models import Entrada
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario
from produtos.models import Produtos

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



class PesquisaEntradaForm(forms.Form):
    termo = forms.CharField(
        label="Buscar",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite nome, marca ou descrição...',
            'class': 'form-control'
        })
    )
    funcionario = forms.ModelChoiceField(
        queryset=Funcionario.objects.all(),
        required=False,
        label="Funcionario",
        empty_label="Todas os funcionarios",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
