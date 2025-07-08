from django.test import TestCase, Client
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from funcionarios.models import Funcionario, Funcao
from fornecedores.models import Fornecedor
from entrada.models import Entrada 

class CadastrarEntradaViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.categoria = Categorias.objects.create(nome="Eletrônicos")
        self.marca = Marca.objects.create(nome="Samsung")
        self.modelo = Modelo.objects.create(nome="Galaxy S22", marca=self.marca)
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste",
            contato="Contato Teste",
            endereco="Endereco Teste",
        )

        self.produto_teste = Produtos.objects.create(
            nome="Produto Teste para Entrada",
            fornecedor = self.fornecedor,
            cor="Azul",
            tamanho=7.0,
            modelo=self.modelo,
            marca=self.marca,
            descricao="Um produto para testes de entrada.",
            categoria=self.categoria
        )

        self.fornecedor = Fornecedor.objects.create(
        nome="Fornecedor Teste",
        contato="Contato Teste00",
        endereco="Endereco Teste",
        )

        self.funcao = Funcao.objects.create(nome="Cargo Teste", salario=1000.0)  # Criar funcao

        self.funcionario = Funcionario.objects.create(
            nome="Funcionario Teste", 
            funcao=self.funcao, 
            telefone="84999999999",
        )

    def test_cadastrar_entrada_view_post(self):
        print("test_cadastrar_entrada_view_post")

        data = {
            "quantidade": 10,
            "valor": 250.00,
            "produto": self.produto_teste.id,
            "fornecedor": self.fornecedor.id,
            "funcionario": self.funcionario.id
        }

        response = self.client.post(reverse("cadastrar_entrada"), data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('listar_entrada'))

        self.assertEqual(Entrada.objects.count(), 1)
        created_entrada = Entrada.objects.first()
        self.assertEqual(created_entrada.quantidade, 10)
        self.assertEqual(created_entrada.valor, 250.00)
        self.assertEqual(created_entrada.produto, self.produto_teste)

    def test_cadastrar_entrada_view_get(self):
        print("test_cadastrar_entrada_view_get")
        ## Teste para o GET da view cadastrar_entrada
        response = self.client.get(reverse("cadastrar_entrada"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastrar_entrada.html")
    
    def test_cadastrar_entrada_sem_quantidade(self):
        print("test_cadastrar_entrada_sem_quantidade")
        initial_entrada_count = Entrada.objects.count()

        data = {
            'quantidade': '',
            "valor": 250.00,
            "produto": self.produto_teste.id,
            "fornecedor": self.fornecedor.id,
            "funcionario": self.funcionario.id
        }
        response = self.client.post(reverse("cadastrar_entrada"), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastrar_entrada.html")
        self.assertContains(response, "Este campo é obrigatório.")
        self.assertEqual(Entrada.objects.count(), initial_entrada_count)


    def test_cadastrar_entrada_sem_funcionario(self):
        print("test_cadastrar_entrada_sem_funcionario")
        initial_entrada_count = Entrada.objects.count()

        data = {
            'quantidade': 10,
            "valor": 250.00,
            "produto": self.produto_teste.id,
            "fornecedor": self.fornecedor.id,
            "funcionario": ''  # Campo obrigatório omitido
        }
        response = self.client.post(reverse("cadastrar_entrada"), data)

        self.assertEqual(response.status_code, 200)  # Não redireciona
        self.assertTemplateUsed(response, "cadastrar_entrada.html")
        self.assertContains(response, "Este campo é obrigatório.")  # Erro esperado
        self.assertEqual(Entrada.objects.count(), initial_entrada_count)  # Nenhuma entrada criada
