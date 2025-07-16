from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
  class Meta:
    model = Venda
    fields = ['funcionario', 'cliente', 'entrada', 'preco']  # Removido 'data'
  
  def __init__(self, *args, **kwargs):
    super(VendaForm, self).__init__(*args, **kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs.update({'class': 'form-control'})
