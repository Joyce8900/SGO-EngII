from django.db import models
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario
from produtos.models import Produtos
from django.core.validators import MinValueValidator

# Create your models here.
class Entrada(models.Model):
  data_entrada = models.DateTimeField(auto_now_add=True)
  quantidade = models.PositiveIntegerField( validators=[MinValueValidator(1)],null=False, blank=False)
  valor = models.FloatField(validators=[MinValueValidator(1.0)], null=False, blank=False)
  produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
  fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, blank=True, null=True)
  funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Entrada'
    verbose_name_plural = 'Entradas'
    ordering = ['data_entrada']

 
  def __str__(self):
    return f"{self.produto.nome} - {self.data_entrada.strftime('%d/%m/%Y %H:%M')}"
