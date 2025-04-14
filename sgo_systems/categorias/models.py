from django.db import models

# Create your models here.
class Categorias (models.Model):
  nome = models.CharField(max_length=100, blank=False, null=False, help_text='Este campo é obrigatório')

  def __str__(self):
    return self.nome
