from django import forms
from .models import Produtos, Categorias


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ['nome', 'fornecedor',  'cor', 'tamanho', 'marca', 'descricao', 'categoria', 'modelo' ]
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço (R$)',
            'quantidade': 'Quantidade',
            'cor': 'Cor',
            'tamanho': 'Tamanho',
            'marca': 'Marca',
            'descricao': 'Descrição',
        }
        widgets = {
            'nome': forms.TextInput(),
            'descricao': forms.Textarea(),
        }


class PesquisaProdutoForm(forms.Form):
    termo = forms.CharField(
        label="Buscar",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    
    categoria = forms.ModelChoiceField(
        queryset=Categorias.objects.all(),
        required=False,
        label="Categoria",
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Todas as categorias"
    )