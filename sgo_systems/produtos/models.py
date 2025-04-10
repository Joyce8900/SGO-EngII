from django.db import models 


  
class Produtos(models.Model):
  nome = models.CharField(max_length=100, blank=False, null=False, help_text='Este campo é obrigatório')
  preco = models.FloatField(null=False, help_text="Insira o valor do produto")
  quantidade = models.IntegerField(null=False, help_text="Insira a quantidade.")
  # categoria = models.ForeignKey('categorias.Categorias', on_delete=models.PROTECT, help_text="Selecione uma categoria.")
  cor = models.CharField(max_length=30)
  tamanho = models.CharField(max_length=100)
  marca = models.CharField(max_length=100)  
  descricao = models.CharField(max_length=1000)
  marca = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nome

