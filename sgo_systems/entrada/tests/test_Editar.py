from django.test import TestCase, Client
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from funcionarios.models import Funcionario, Funcao
from fornecedores.models import Fornecedor
from entrada.models import Entrada
from django.contrib.auth.models import User # Adicione esta importação


class EditarEntradaViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Crie um usuário de teste e faça login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.categoria = Categorias.objects.create(nome="Eletrônicos Edit")
        self.marca = Marca.objects.create(nome="Marca Edit")
        self.modelo = Modelo.objects.create(nome="Modelo Edit", marca=self.marca)

        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste",
            contato="Contato Teste1111",
            endereco="Endereco Teste",
        )

        self.fornecedor_edit = Fornecedor.objects.create(
            nome="Fornecedor Edit Teste",
            contato="Contato Edit Teste",
            endereco="Endereco Edit Teste",
        )

        self.produto_para_editar = Produtos.objects.create(
            nome="Produto Teste para Editar Entrada",
            cor="Preto",
            tamanho=8.0,
            modelo=self.modelo,
            marca=self.marca,
            descricao="Um produto para testes de edição de entrada.",
            categoria=self.categoria,
            quantidade=100, # CORRIGIDO AQUI: Adicione uma quantidade inicial alta
        )

        self.funcao_edit = Funcao.objects.create(nome="Cargo Edit Teste", salario=1500.0)

        self.funcionario_edit = Funcionario.objects.create(
            nome="Funcionario Edit Teste",
            funcao=self.funcao_edit,
            telefone="84888888888",
        )

        self.entrada_para_editar = Entrada.objects.create(
            quantidade=20,
            valor=3000.00,
            produto=self.produto_para_editar,
            fornecedor=self.fornecedor_edit,
            funcionario=self.funcionario_edit
        )

        self.produto_para_editar.refresh_from_db()

    def test_editar_entrada_view_post(self):
        print("test_editar_entrada_view_post")

        data_atualizada = {
            "quantidade": 10,
            "valor": 3000.00,
            "produto": self.produto_para_editar.id,
            "fornecedor": self.fornecedor_edit.id,
            "funcionario": self.funcionario_edit.id
        }

        response = self.client.post(
            reverse("entrada:editar_entrada", args=[self.entrada_para_editar.id]), # CORRIGIDO AQUI
            data=data_atualizada
        )

        self.assertEqual(response.status_code, 302)

        self.entrada_para_editar.refresh_from_db()
        self.assertEqual(self.entrada_para_editar.quantidade, 10)
        self.assertEqual(self.entrada_para_editar.valor, 3000.00)

    def test_editar_entrada_view_post_invalido(self):
        print("test_editar_entrada_view_post_invalido")

        data = {
            "produto": self.produto_para_editar.id,
            "funcionario": self.funcionario_edit.id,
            "valor": -10,  # valor inválido
            "quantidade": 0,  # quantidade inválida
            "fornecedor": self.fornecedor_edit.id,
        }

        response = self.client.post(
            reverse("entrada:editar_entrada", args=[self.entrada_para_editar.id]), # CORRIGIDO AQUI
            data
        )

        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertEqual(Entrada.objects.count(), 1)