from django.test import TestCase, Client # Garanta Client importado
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from fornecedores.models import Fornecedor
from django.contrib.auth.models import User # Adicione esta importação

class ExcluirProdutoViewTests(TestCase):
    def setUp(self):
        self.client = Client() # Adicione esta linha
        # Crie um usuário de teste e faça login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword') # Adicione esta linha
        self.client.login(username='testuser', password='testpassword') # Adicione esta linha

        self.marca = Marca.objects.create(nome='Marca Teste')
        self.modelo = Modelo.objects.create(nome='Modelo Teste', marca=self.marca)
        self.categoria = Categorias.objects.create(nome='Categoria Teste')
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            contato='Contato Teste',
            endereco='Endereco Teste'
        )
        self.produto = Produtos.objects.create(
            nome='Produto Teste',
            # REMOVIDO: fornecedor=self.fornecedor, # <--- Removido este argumento
            categoria=self.categoria,
            marca=self.marca,
            descricao='Descrição Teste',
            tamanho=0.5,
            modelo=self.modelo,
            quantidade=10, # Adicione uma quantidade inicial válida
            preco=100.00, # Adicione um preço inicial válido
        )

    def test_excluir_produto_view(self):
        print("test_excluir_produto_view")
        url = reverse('produtos:excluir_produto', args=[self.produto.id]) # CORRIGIDO AQUI
        response = self.client.post(url) # Mude para POST se sua view de exclusão aceita POST (melhor prática)
        self.assertEqual(response.status_code, 302)  # Redirecionamento esperado
        self.assertFalse(Produtos.objects.filter(id=self.produto.id).exists())  # Produto excluído

    def test_excluir_produto_inexistente(self):
        print("test_excluir_produto_inexistente")
        response = self.client.post(reverse('produtos:excluir_produto', args=[999])) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 404) # Produto com ID 999 não existe