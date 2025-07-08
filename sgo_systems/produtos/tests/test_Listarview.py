from django.test import TestCase
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from fornecedores.models import Fornecedor

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
        marca = Marca.objects.create(nome='Marca Testedddd')
        modelo = Modelo.objects.create(nome='Modelo Testes', marca=marca)
        categoria = Categorias.objects.create(nome='Categoria Testes')
        fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            contato='Contato Teste',
            endereco='Endereco Teste',
        )

        Produtos.objects.create(
            nome='Produtos A',
            fornecedor=fornecedor,
            categoria=categoria,
            marca=marca,
            descricao='Descrição A',
            tamanho=0.5,
            modelo=modelo,
        )
        Produtos.objects.create(
            nome='Produtos B',
            fornecedor=fornecedor,
            categoria=categoria,
            marca=marca,
            descricao='Descrição B',
            tamanho=0.5,
            modelo=modelo,
        )

        response = self.client.get(reverse('listar_produtos') + '?termo=Produtos A')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produtos A')
        self.assertNotContains(response, 'Produtos B')

    def test_listar_produto_categoria(self):
        print("test_listar_produto_categoria")
        marca = Marca.objects.create(nome='Marca Testedddd1')
        modelo = Modelo.objects.create(nome='Modelo Testes1', marca=marca)
        categoria1 = Categorias.objects.create(nome='Categoria1')
        categoria2 = Categorias.objects.create(nome='Categoria2')
        fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste2',
            contato='Contato Teste2',
            endereco='Endereco Teste2',
        )

        Produtos.objects.create(
            nome='Produtos A',
            fornecedor=fornecedor,
            categoria=categoria1,
            marca=marca,
            descricao='Descrição A',
            tamanho=0.5,
            modelo=modelo,
        )
        Produtos.objects.create(
            nome='Produtos B',
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
        self.assertContains(response, 'Produtos A')
        self.assertNotContains(response, 'Produtos B')

    def test_listar_produtos_sem_produtos(self):
        print("test_listar_produtos_sem_produtos")
        Produtos.objects.all().delete()
        response = self.client.get(reverse('listar_produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhum produto cadastrado")  
