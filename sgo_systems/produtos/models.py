from django.db import models 
from django.core.validators import MinValueValidator
from categorias.models import Categorias
  
class Produtos(models.Model):
  categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
  nome = models.CharField(max_length=100, blank=False, null=False, help_text='Este campo é obrigatório')
  preco = models.FloatField(null=False, help_text="Insira o valor do produto", validators=[MinValueValidator(1.0)])
  quantidade = models.IntegerField(null=False, help_text="Insira a quantidade.", validators=[MinValueValidator(1)])
  cor = models.CharField(max_length=30)
  tamanho = models.FloatField(max_length=100, validators=[MinValueValidator(0.01)])
  marca = models.CharField(max_length=100)  
  descricao = models.CharField(max_length=1000)
  
  
  def __str__(self):
    return f'{self.nome} , {self.categoria.nome()}'
