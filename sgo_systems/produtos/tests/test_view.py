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
        ## Teste para o GET da view cadastrar_produto
        response = self.client.get(reverse("cadastrar_produto"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastrar_produto.html")

    def test_cadastrar_produto_view_post_invalido(self):
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
