from django.test import TestCase
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca

class CadastrarProdutoViewTests(TestCase):
    def setUp(self):
        self.categoria = Categorias.objects.create(nome="Eletrônicos")
        self.marca = Marca.objects.create(nome="Samsung")
        self.modelo = Modelo.objects.create(nome="Galaxy S22", marca=self.marca)

    def test_cadastrar_produto_view_post(self):
        print("test_cadastrar_produto_view_post")
        ## Teste para o POST da view cadastrar_produto
        data = {
            "categoria": self.categoria.id,
            "nome": "Oculos",
            "preco": 2500.00,
            "quantidade": 10,
            "cor": "Preto",
            "tamanho": 6.5,
            "modelo": self.modelo.id,
            "marca": self.marca.id,
            "descricao": "Um oculos moderno para uso dia a dia.",
        }
        response = self.client.post(reverse("cadastrar_produto"), data)
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertEqual(Produtos.objects.count(), 1)  # Produto salvo
        self.assertEqual(Produtos.objects.first().nome, "Oculos")

    def test_cadastrar_produto_view_get(self):
        print("test_cadastrar_produto_view_get")
        ## Teste para o GET da view cadastrar_produto
        response = self.client.get(reverse("cadastrar_produto"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastrar_produto.html")

    def test_cadastrar_produto_view_post_invalido(self):
      print("test_cadastrar_produto_view_post_invalido")
    # Dados inválidos: faltando campos obrigatórios
      data = {
          "nome": "",  
          "preco": -10,  
          "quantidade": 0,  # Quantidade inválida (MinValueValidator exige >= 1)
          # categoria, modelo e marca não enviados (obrigatórios)
      }
      response = self.client.post(reverse("cadastrar_produto"), data)
      self.assertEqual(response.status_code, 200)
      form = response.context["form"]
      self.assertFalse(form.is_valid())
      self.assertIn("nome", form.errors)
      self.assertIn("Este campo é obrigatório.", form.errors["nome"])
      self.assertEqual(Produtos.objects.count(), 0)

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
      Produtos.objects.create(
          nome='Produtos A',
          preco=10.0,
          quantidade=5,  
          categoria=self.categoria,
          marca=self.marca,
          descricao='Descrição A',
          tamanho=0.5,
          modelo=self.modelo,
      )


      Produtos.objects.create(
          nome='Produtos B',
          preco=20.0,
          quantidade=10,  
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
      Produtos.objects.create(
          nome='Produtos A',
          preco=10.0,
          quantidade=5,  
          categoria=self.categoria,
          marca=self.marca,
          descricao='Descrição A',
          tamanho=0.5,
          modelo=self.modelo,
      )
      Produtos.objects.create(
          nome='Produtos B',
          preco=20.0,
          quantidade=10,  
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
  
