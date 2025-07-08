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
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            contato='Contato Teste',
            endereco='Endereco Teste',
        )
      
    def test_listar_produtos_view(self):
        print("test_listar_produtos_view")
        response = self.client.get(reverse("listar_produtos"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_produtos.html")
        self.assertQuerySetEqual(
            response.context["produtos"],
            Produtos.objects.all().order_by("nome"),
            transform=lambda p: p
        )

    def test_listar_produtos_com_termo(self):
        print("test_listar_produtos_com_termo")

        marca = Marca.objects.create(nome='Marca Teste 2')
        modelo = Modelo.objects.create(nome='Modelo Teste 2', marca=marca)
        categoria = Categorias.objects.create(nome='Categoria Teste 2')
        fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste 2',
            contato=f'{uuid.uuid4()}@teste.com',
            endereco='Endereco Teste 2',
        )
        Produtos.objects.create(
            nome='Produto A',
            fornecedor=fornecedor,
            categoria=categoria,
            marca=marca,
            descricao='Descrição A',
            tamanho=0.5,
            modelo=modelo,
        )
        Produtos.objects.create(
            nome='Produto B',
            fornecedor=fornecedor,
            categoria=categoria,
            marca=marca,
            descricao='Descrição B',
            tamanho=0.5,
            modelo=modelo,
        )

        response = self.client.get(reverse('listar_produtos') + '?termo=Produto A')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto A')
        self.assertNotContains(response, 'Produto B')

    def test_listar_produto_categoria(self):
        print("test_listar_produto_categoria")

        marca = Marca.objects.create(nome='Marca Teste 3')
        modelo = Modelo.objects.create(nome='Modelo Teste 3', marca=marca)
        categoria1 = Categorias.objects.create(nome='Categoria 1')
        categoria2 = Categorias.objects.create(nome='Categoria 2')
        fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste 3',
            contato=f'{uuid.uuid4()}@teste.com',
            endereco='Endereco Teste 3',
        )

        Produtos.objects.create(
            nome='Produto A',
            fornecedor=fornecedor,
            categoria=categoria1,
            marca=marca,
            descricao='Descrição A',
            tamanho=0.5,
            modelo=modelo,
        )
        Produtos.objects.create(
            nome='Produto B',
            fornecedor=fornecedor,
            categoria=categoria2,
            marca=marca,
            descricao='Descrição B',
            tamanho=0.5,
            modelo=modelo,
        )

        url = reverse('listar_produtos') + f'?categoria={categoria1.id}'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto A')
        self.assertNotContains(response, 'Produto B')

    def test_listar_produtos_sem_produtos(self):
        print("test_listar_produtos_sem_produtos")
        Produtos.objects.all().delete()
        response = self.client.get(reverse('listar_produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhum produto cadastrado")
