from django.db import models

# Create your models here.
class Entrada(models.Model):
  data_entrada = models.DateField()
  quantidade = models.PositiveIntegerField()
  valor = models.FloatField()
  fornecedor = models.ForeignKey('fornecedores.Fornecedores', on_delete=models.CASCADE)
  funcionario = models.ForeignKey('funcionarios.Funcionarios', on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Entrada'
    verbose_name_plural = 'Entradas'
    ordering = ['data_entrada']

  def __str__(self):
    return self.data_entrada