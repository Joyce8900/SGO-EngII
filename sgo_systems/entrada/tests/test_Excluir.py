from django.test import TestCase, Client
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from funcionarios.models import Funcionario
from fornecedores.models import Fornecedor
from entrada.models import Entrada
from django.shortcuts import get_object_or_404
class ExcluirEntradaViewTests(TestCase):
  def test_excluir_entrada(self):
    #Teste para excluir uma entrada existente
    print("test_excluir_entrada")
    self.marca = Marca.objects.create(nome='Marca Teste')
    self.modelo = Modelo.objects.create(nome='Modelo Teste', marca=self.marca)  
    self.categoria = Categorias.objects.create(nome='Categoria Teste')
    self.produto = Produtos.objects.create(
        nome='Produto Teste',
        preco=10.0,
        quantidade=5,  
        categoria=self.categoria,
        marca=self.marca,
        descricao='Descrição Teste',
        tamanho=0.5,
        modelo=self.modelo,
    )
    self.fornecedor = Fornecedor.objects.create(
        nome="Fornecedor Teste",
        contato="Contato Teste",
        endereco="Endereco Teste",
    )
    self.funcionario = Funcionario.objects.create(
        nome="Funcionario Teste",
        cargo="Cargo Teste",
        telefone="84888888888",
    )
    self.entrada = Entrada.objects.create(
        fornecedor=self.fornecedor,
        funcionario=self.funcionario,
        produto=self.produto,
        quantidade=10,
        valor=10.0
    )
    url = reverse('excluir_entrada', args=[self.entrada.id])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 302)
    self.assertFalse(Entrada.objects.filter(id=self.entrada.id).exists())
  
  def test_excluir_entrada_inexistente(self):
    # Teste para excluir uma entrada inexistente
    print("test_excluir_entrada_inexistente")
    
    response = self.client.post(reverse('excluir_entrada', args=[999]))
    self.assertEqual(response.status_code, 404)