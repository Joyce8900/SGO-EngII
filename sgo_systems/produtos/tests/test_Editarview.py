from django.test import TestCase, Client # Garanta Client importado
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from fornecedores.models import Fornecedor
from django.contrib.auth.models import User # Adicione esta importação

class EditarProdutoViewTests(TestCase):
    def setUp(self):
        self.client = Client() # Adicione esta linha
        # Crie um usuário de teste e faça login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword') # Adicione esta linha
        self.client.login(username='testuser', password='testpassword') # Adicione esta linha
        
        self.categoria = Categorias.objects.create(nome="Eletrônicos")
        self.marca = Marca.objects.create(nome="Samsung")
        self.modelo = Modelo.objects.create(nome="Galaxy S22", marca=self.marca)
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste",
            contato="Contato Teste",
            endereco="Endereco Teste",
        )

        self.produto = Produtos.objects.create(
            nome="Oculos",
            categoria=self.categoria,
            # REMOVIDO: fornecedor=self.fornecedor, # <--- Removido este argumento
            cor="Preto",
            tamanho=6.5,
            modelo=self.modelo,
            marca=self.marca,
            descricao="Um oculos moderno para uso dia a dia.",
            quantidade=10, # Adicione uma quantidade inicial válida
            preco=100.00, # Adicione um preço inicial válido
        )

    def test_editar_produto_view_post(self):
        print("test_editar_produto_view_post")

        data_atualizada = {
            "categoria": self.categoria.id,
            "nome": "Óculos Atualizado",
            # REMOVIDO: "fornecedor": self.fornecedor.id, # <--- Removido este argumento
            "cor": "Azul",
            "tamanho": 6.5,
            "modelo": self.modelo.id,
            "marca": self.marca.id,
            "descricao": "Atualizado para teste.",
            "quantidade": 15, # Garanta que a quantidade é válida após a edição
            "preco": 2600.00,
        }

        response = self.client.post(
            reverse("produtos:editar_produto", args=[self.produto.id]), data=data_atualizada # CORRIGIDO AQUI
        )

        self.assertEqual(response.status_code, 302)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, "Óculos Atualizado")

    def test_editar_produto_view_get(self):
        print("test_editar_produto_view_get")
        response = self.client.get(reverse("produtos:editar_produto", args=[self.produto.id])) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "editar_produto.html") # CORRIGIDO CAMINHO DO TEMPLATE

    def test_editar_produto_view_post_invalido(self):
        print("test_editar_produto_view_post_invalido")
        data = {
            "nome": "",  # Campo obrigatório vazio
        }
        response = self.client.post(reverse("produtos:editar_produto", args=[self.produto.id]), data) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)
        self.assertIn("Este campo é obrigatório.", form.errors["nome"])
        self.assertEqual(Produtos.objects.count(), 1)