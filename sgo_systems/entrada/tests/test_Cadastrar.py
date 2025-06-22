from django.test import TestCase, Client
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from funcionarios.models import Funcionario
from fornecedores.models import Fornecedor
from entrada.models import Entrada 

class CadastrarEntradaViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.categoria = Categorias.objects.create(nome="Eletrônicos")
        self.marca = Marca.objects.create(nome="Samsung")
        self.modelo = Modelo.objects.create(nome="Galaxy S22", marca=self.marca)

        self.produto_teste = Produtos.objects.create(
            nome="Produto Teste para Entrada",
            preco=100.00,
            quantidade=50,
            cor="Azul",
            tamanho=7.0,
            modelo=self.modelo,
            marca=self.marca,
            descricao="Um produto para testes de entrada.",
            categoria=self.categoria
        )

        self.fornecedor = Fornecedor.objects.create(
        nome="Fornecedor Teste",
        contato="Contato Teste",
        endereco="Endereco Teste",
        )

        self.funcao = Funcao.objects.create(nome="Cargo Teste")  # Criar funcao

        self.funcionario = Funcionario.objects.create(
            nome="Funcionario Teste",
            funcao=self.funcao,  # usar funcao
            telefone="84999999999",
        )

    def test_cadastrar_entrada_view_post(self):
        print("test_cadastrar_entrada_view_post") # Alterado o print
        ## Teste para o POST da view cadastrar_entrada
        initial_product_quantity = self.produto_teste.quantidade # Pega a quantidade inicial do produto

        data = {
            # Estes são os campos esperados pelo seu EntradaForm
            "quantidade": 10,
            "valor": 250.00, # Exemplo: 10 * 25 (se o preço do produto fosse 25)
            "produto": self.produto_teste.id, # Use o ID do produto criado
            "fornecedor": self.fornecedor.id,
            "funcionario": self.funcionario.id
        }
        response = self.client.post(reverse("cadastrar_entrada"), data, follow=True) # follow=True para seguir o redirecionamento

        # Asserções para um POST bem-sucedido
        self.assertEqual(response.status_code, 200) 
        self.assertRedirects(response, reverse('listar_entrada')) # Verifica se o redirecionamento ocorreu corretamente

        # Verifica se um objeto Entrada foi criado
        self.assertEqual(Entrada.objects.count(), 1)
        created_entrada = Entrada.objects.first()
        self.assertEqual(created_entrada.quantidade, 10)
        self.assertEqual(created_entrada.valor, 250.00)
        self.assertEqual(created_entrada.produto, self.produto_teste)

        # Verifica se a quantidade do produto foi atualizada
        self.produto_teste.refresh_from_db() # Recarrega o produto do banco de dados
        self.assertEqual(self.produto_teste.quantidade, initial_product_quantity + 10) # Verifica se a quantidade do produto foi atualizada
 
    def test_cadastrar_entrada_view_get(self):
        print("test_cadastrar_entrada_view_get")
        ## Teste para o GET da view cadastrar_entrada
        response = self.client.get(reverse("cadastrar_entrada"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastrar_entrada.html")
    
    def test_cadastrar_entrada_sem_quantidade(self):
        print("test_cadastrar_entrada_sem_quantidade")
        initial_entrada_count = Entrada.objects.count()
        initial_product_quantity = self.produto_teste.quantidade

        data = {
            'quantidade': '',
            "valor": 250.00,
            "produto": self.produto_teste.id,
            "fornecedor": self.fornecedor.id,
            "funcionario": self.funcionario.id
        }
        response = self.client.post(reverse("cadastrar_entrada"), data)

        self.assertEqual(response.status_code, 200)  # Não redireciona, permanece na página
        self.assertTemplateUsed(response, "cadastrar_entrada.html")
        self.assertContains(response, "Este campo é obrigatório.") # Mensagem de erro padrão do Django
        self.assertEqual(Entrada.objects.count(), initial_entrada_count) # Nenhuma entrada deve ser criada

        self.produto_teste.refresh_from_db()
        self.assertEqual(self.produto_teste.quantidade, initial_product_quantity) # Estoque não deve mudar


    def test_cadastrar_entrada_sem_funcionario(self):
        print("test_cadastrar_entrada_sem_funcionario")
        initial_entrada_count = Entrada.objects.count()
        initial_product_quantity = self.produto_teste.quantidade

        data = {
            'quantidade': 10,
            "valor": 250.00,
            "produto": self.produto_teste.id,
            "fornecedor": self.fornecedor.id,
            "funcionario": '' #Para teste
        }
        response = self.client.post(reverse("cadastrar_entrada"), data)

        self.assertEqual(response.status_code, 200)  # Não redireciona, permanece na página
        self.assertTemplateUsed(response, "cadastrar_entrada.html")
        self.assertContains(response, "Este campo é obrigatório.") # Mensagem de erro padrão do Django
        self.assertEqual(Entrada.objects.count(), initial_entrada_count) # Nenhuma entrada deve ser criada

        self.produto_teste.refresh_from_db()
        self.assertEqual(self.produto_teste.quantidade, initial_product_quantity) # Estoque não deve mudar