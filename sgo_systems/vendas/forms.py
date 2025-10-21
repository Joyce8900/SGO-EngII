from django import forms
from django_select2.forms import Select2Widget, ModelSelect2Widget
from .models import Venda, ItemVenda
from produtos.models import Produtos
from django.forms import inlineformset_factory


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control'})
        }
    
    
ItemVendaFormSet = inlineformset_factory(
    Venda, ItemVenda, form=ItemVendaForm, extra=1, can_delete=True
)


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'funcionario']
        labels = {
            'cliente': 'Cliente',
            'funcionario': 'Funcionário',
        }
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
        }