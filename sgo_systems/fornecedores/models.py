from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.TextField(verbose_name='Endereço', blank=True, null=True)
    contato = models.CharField(max_length=100, verbose_name='Contato')
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome