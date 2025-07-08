from django.test import TestCase
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from fornecedores.models import Fornecedor

class ExcluirProdutoViewTests(TestCase):
    def setUp(self):
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
            fornecedor=self.fornecedor,
            categoria=self.categoria,
            marca=self.marca,
            descricao='Descrição Teste',
            tamanho=0.5,
            modelo=self.modelo,
        )

    def test_excluir_produto_view(self):
        print("test_excluir_produto_view")
        url = reverse('excluir_produto', args=[self.produto.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirecionamento esperado
        self.assertFalse(Produtos.objects.filter(id=self.produto.id).exists())  # Produto excluído

    def test_excluir_produto_inexistente(self):
        print("test_excluir_produto_inexistente")
        response = self.client.post(reverse('excluir_produto', args=[999]))
        self.assertEqual(response.status_code, 404)  # Produto com ID 999 não existe
