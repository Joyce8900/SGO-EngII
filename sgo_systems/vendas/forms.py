# vendas/forms.py
from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from .models import Venda
from produtos.models import Produtos

class ProdutoWidget(ModelSelect2MultipleWidget):
    model = Produtos
    search_fields = [
        'nome__icontains',
        'categoria__nome__icontains',
    ]
    
    def label_from_instance(self, obj):
        return f"{obj.nome} - {obj.categoria.nome} - R$ {obj.preco:.2f}"

class VendaForm(forms.ModelForm):
    itens = forms.ModelMultipleChoiceField(
        queryset=Produtos.objects.select_related('categoria').all(),
        widget=ProdutoWidget(
            attrs={
                'class': 'form-control',
                'data-placeholder': 'Digite para pesquisar produtos...',
            }
        ),
        label='Produtos',
    )
    
    valor_total = forms.DecimalField(
        label='Valor Total',
        required=False,
        disabled=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )
    
    class Meta:
        model = Venda
        fields = ['cliente', 'funcionario', 'itens', 'valor_total']
        labels = {
            'cliente': 'Cliente',
            'funcionario': 'Funcionário',
        }
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            instance.save()
            self.save_m2m()
            
            valor_total = sum(item.preco for item in instance.itens.all())
            instance.valor_total = valor_total
            instance.save()
        
        return instance
