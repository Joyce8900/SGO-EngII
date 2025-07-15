from django import forms
from .models import Produtos, Categorias

    
class ProdutoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classes CSS consistentes a todos os campos
        for field_name, field in self.fields.items():
            if field_name in ['cor', 'tamanho', 'marca', 'categoria', 'modelo']:
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
            
            # Configurações específicas por campo
            if field_name == 'descricao':
                field.widget.attrs.update({'rows': 3})
            elif field_name == 'preco':
                field.widget.attrs.update({
                    'min': '0.01',
                    'step': '0.01',
                })
            elif field_name == 'quantidade':
                field.widget.attrs.update({
                    'min': '1',
                })

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
        fields = [
            'nome', 'preco', 'quantidade', 'cor', 
            'tamanho', 'marca', 'descricao', 'categoria', 'modelo'
        ]
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço (R$)',
            'quantidade': 'Quantidade',
            'cor': 'Cor',
            'tamanho': 'Tamanho',
            'marca': 'Marca',
            'descricao': 'Descrição',
            'categoria': 'Categoria',
            'modelo': 'Modelo'
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