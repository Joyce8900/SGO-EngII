from django.test import TestCase
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from fornecedores.models import Fornecedor


class EditarProdutoViewTests(TestCase):
    
    def setUp(self):
        self.categoria = Categorias.objects.create(nome="Eletrônicos")
        self.marca = Marca.objects.create(nome="Samsung")
        self.modelo = Modelo.objects.create(nome="Galaxy S22", marca=self.marca)
        self.fornecedor = Fornecedor.objects.create(nome="Fornecedor Teste") 

        self.produto = Produtos.objects.create(
            nome="Oculos",
            categoria=self.categoria,
            cor="Preto",
            fornecedor=self.fornecedor,
            tamanho=6.5,
            modelo=self.modelo,
            marca=self.marca,
            descricao="Um oculos moderno para uso dia a dia.",
        )

    def test_editar_produto_view_post(self):
        ## Teste para o POST da view editar_produto
        print("test_editar_produto_view_post")

        data_atualizada = {
            "categoria": self.categoria.id,
            "nome": "Óculos Atualizado",
            "fornecedor": self.fornecedor.id,
            "cor": "Azul",
            "tamanho": 6.5,
            "modelo": self.modelo.id,
            "marca": self.marca.id,
            "descricao": "Atualizado para teste.",
        }

        response = self.client.post(
            reverse("editar_produto", args=[self.produto.id]), data=data_atualizada
        )

        self.assertEqual(response.status_code, 302)

        # Atualize os dados do produto para o que foi salvo no banco
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, "Óculos Atualizado")
        

    def test_editar_produto_view_get(self):
        print("test_editar_produto_view_get")
         ## Teste para o GET da view editar_produto
        response = self.client.get(reverse("editar_produto",args=[self.produto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "editar_produto.html")

    def test_editar_produto_view_post_invalido(self):
      print("test_editar_produto_view_post_invalido")
     # Dados inválidos: faltando campos obrigatórios
      data = {
           "nome": "",  
          
          }
      response = self.client.post(reverse("editar_produto", args=[self.produto.id]), data)
      self.assertEqual(response.status_code, 200)
      form = response.context["form"]
      self.assertFalse(form.is_valid())
      self.assertIn("nome", form.errors)
      self.assertIn("Este campo é obrigatório.", form.errors["nome"])
      self.assertEqual(Produtos.objects.count(), 1)

