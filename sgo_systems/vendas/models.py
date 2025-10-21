# vendas/models.py
from django.db import models
from cliente.models import Cliente
# Make sure these imports match your actual app and model names
from funcionarios.models import Funcionario # Assuming you have a 'funcionario' app and Funcionario model
from produtos.models import Produtos      # Assuming you have a 'produto' app and Produto model

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vendas_cliente')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True, related_name='vendas_funcionario')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    data = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Venda #{self.pk} - {self.cliente.nome} ({self.data.strftime("%d/%m/%Y")})'
    

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens_venda')
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal (self):
        return self.produto.preco * self.quantidade