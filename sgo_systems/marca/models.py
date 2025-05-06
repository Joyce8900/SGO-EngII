from django.db import models

class Marca (models.Model):
  nome = models.CharField(unique=True,max_length=50, blank=False, null=False)

  def __str__(self):
    return self.nome