from django.test import TestCase
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from fornecedores.models import Fornecedor
import uuid
class ListarProdutoViewTests(TestCase):
    
    def setUp(self):
        self.categoria = Categorias.objects.create(nome='Categoria Teste')
        self.marca = Marca.objects.create(nome='Marca Teste')
      
    def test_listar_produtos_view(self):
        print("test_listar_produtos_view")
        ## Teste para o GET da view listar_produtos
        response = self.client.get(reverse("listar_produtos"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_produtos.html")
        self.assertQuerySetEqual(response.context["produtos"], Produtos.objects.all().order_by("nome"), transform=lambda p: p)                              
    

    def test_listar_produtos_com_termo(self):
      print("test_listar_produtos_com_termo")
    ## Teste para o GET da view listar_produtos com termo
    # Supondo que 'Produto A' e 'Produto B' existem no banco de dados
      self.marca = Marca.objects.create(nome='Marca Testedddd')
      self.modelo = Modelo.objects.create(nome='Modelo Testes', marca=self.marca)
      self.categoria = Categorias.objects.create(nome='Categoria Testes')
      self.fornecedor = Fornecedor.objects.create(
          nome='Fornecedor Teste',
          contato=f'{uuid.uuid4()}@teste.com',
          endereco='Endereco Teste',
      )
      Produtos.objects.create(
          nome='Produtos A',
          fornecedor = self.fornecedor,  
          categoria=self.categoria,
          marca=self.marca,
          descricao='Descrição A',
          tamanho=0.5,
          modelo=self.modelo,
      )


      Produtos.objects.create(
          nome='Produtos B',
          fornecedor = self.fornecedor, 
          categoria=self.categoria,
          marca=self.marca,
          descricao='Descrição B',
          tamanho=0.5,
          modelo=self.modelo,
      )

      response = self.client.get(reverse('listar_produtos') + '?termo=Produtos A')
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, 'Produtos A')
      self.assertNotContains(response, 'Produtos B')

    def test_listar_produto_categoria(self):
      print("test_listar_produto_categoria")
    ## Teste para o GET da view listar_produtos com categoria
      self.marca = Marca.objects.create(nome='Marca Testedddd1')
      self.modelo = Modelo.objects.create(nome='Modelo Testes1', marca=self.marca)
      self.categoria = Categorias.objects.create(nome='Categoria1')
      self.categoria2 = Categorias.objects.create(nome='Categoria2')
      self.fornecedor = Fornecedor.objects.create(
          nome='Fornecedor Teste',
          contato=f'{uuid.uuid4()}@teste.com',
          endereco='Endereco Teste',
      )
      self.fornecedor2 = Fornecedor.objects.create(
          nome='Fornecedor Teste2',
          contato= f'{uuid.uuid4()}@teste.com',
          endereco='Endereco Teste2',
      )
      Produtos.objects.create(
          nome='Produtos A',
          fornecedor = self.fornecedor,
          categoria=self.categoria,
          marca=self.marca,
          descricao='Descrição A',
          tamanho=0.5,
          modelo=self.modelo,
      )
      Produtos.objects.create(
          nome='Produtos B',
          fornecedor = self.fornecedor2, 
          categoria=self.categoria2,
          marca=self.marca,
          descricao='Descrição B',
          tamanho=0.5,
          modelo=self.modelo,
      )
      url = reverse('listar_produtos') + f'?categoria={self.categoria.id}'
      response = self.client.get(url)
      
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, 'Produtos A')
      self.assertNotContains(response, 'Produtos B')


    def test_listar_produtos_sem_produtos(self):
      print("test_listar_produtos_sem_produtos")
      ## Teste para o GET da view listar_produtos sem produtos
      Produtos.objects.all().delete()
      response = self.client.get(reverse('listar_produtos'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "Nenhum produto cadastrado")  
  
