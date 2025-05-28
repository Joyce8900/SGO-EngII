from django.db import models

class Marca (models.Model):
  nome = models.CharField(unique=True,max_length=50, blank=False, null=False, error_messages={'unique': "Já existe uma marca com este nome"}, help_text='Este campo é obrigatório') 

  def __str__(self):
    return self.nome