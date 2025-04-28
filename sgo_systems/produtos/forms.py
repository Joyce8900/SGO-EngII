from django import forms
from .models import Produtos
from .models import Categorias

class ProdutoForm(forms.ModelForm):
    def clean_preco(self):
        preco = self.cleaned_data['preco']
        if preco <= 0:
            raise forms.ValidationError("O preço deve ser maior que zero.")
        return round(preco, 2) 


    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade   
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'quantidade', 'cor', 'tamanho', 'marca', 'descricao', 'categoria' ]
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
            'preco': 'Preço',
        }

class PesquisaProdutoForm(forms.Form):
    termo = forms.CharField(
        label="Buscar",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite nome, marca ou descrição...',
            'class': 'form-control'
        })
    )
    categoria = forms.ModelChoiceField(
        queryset=Categorias.objects.all(),
        required=False,
        label="Categoria",
        empty_label="Todas as categorias"
    )
