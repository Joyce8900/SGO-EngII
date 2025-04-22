from django.db import models

# Create your models here.
class Categorias (models.Model):
  TIPOS_CATEGORIA = [
        ('GRAU', 'Óculos de Grau'),
        ('SOL', 'Óculos de Sol'),
        ('LENTES', 'Lentes de Contato'),
        ('ACESSORIOS', 'Acessórios'),
        ('SAUDE', 'Saúde Ocular'),
        ('INFANTIL', 'Óculos Infantis'),
        ('ESPORTE', 'Óculos Esportivos'),
    ]
  nome = models.CharField(max_length=100, 
                          blank=False, 
                          null=False,
                          help_text='Este campo é obrigatório',
                          choices=TIPOS_CATEGORIA,
                          unique=True)

  def __str__(self):
    return self.get_nome_display()