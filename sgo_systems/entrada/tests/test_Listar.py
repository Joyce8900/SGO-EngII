from django.test import TestCase, Client
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from funcionarios.models import Funcionario, Funcao
from fornecedores.models import Fornecedor
from entrada.models import Entrada


class ListarEntradaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.categoria = Categorias.objects.create(nome='Categoria Teste')
        self.marca = Marca.objects.create(nome='Marca Teste')
        self.modelo = Modelo.objects.create(nome='Modelo Teste', marca=self.marca)
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            contato='Contato Teste',
            endereco='Endereco Teste',
        )
        self.funcao = Funcao.objects.create(nome='Cargo Teste', salario=1300.0)
        self.funcionario = Funcionario.objects.create(
            nome='Funcionario Teste',
            funcao=self.funcao,
            telefone='84999999999'
        )

    def test_listar_entrada_view(self):
        print("test_listar_entrada_view")
        response = self.client.get(reverse("listar_entrada"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_entrada.html")
        self.assertQuerySetEqual(
            response.context["entrada"],
            Entrada.objects.all().order_by("data_entrada"),
            transform=lambda p: p
        )

    def test_listar_entrada_com_termo(self):
        print("test_listar_entrada_com_termo")

        produto_a = Produtos.objects.create(
            nome='Produtos A',
            fornecedor=self.fornecedor,
            categoria=self.categoria,
            marca=self.marca,
            descricao='Descrição A',
            tamanho=0.5,
            modelo=self.modelo,
        )

        produto_b = Produtos.objects.create(
            nome='Produtos B',
            fornecedor=self.fornecedor,
            categoria=self.categoria,
            marca=self.marca,
            descricao='Descrição B',
            tamanho=0.5,
            modelo=self.modelo,
        )

        Entrada.objects.create(
            fornecedor=self.fornecedor,
            funcionario=self.funcionario,
            produto=produto_a,
            quantidade=10,
            valor=100.0,
        )

        Entrada.objects.create(
            fornecedor=self.fornecedor,
            funcionario=self.funcionario,
            produto=produto_b,
            quantidade=10,
            valor=100.0,
        )

        response = self.client.get(reverse('listar_entrada') + '?termo=Produtos A')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produtos A')
        self.assertNotContains(response, 'Produtos B')

    def test_listar_entrada_sem_produtos(self):
        print("test_listar_entrada_sem_produtos")
        response = self.client.get(reverse('listar_entrada'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhuma entrada cadastrada")
