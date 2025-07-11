from django.test import TestCase, Client
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from funcionarios.models import Funcionario, Funcao
from fornecedores.models import Fornecedor
from entrada.models import Entrada


class EditarEntradaViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.categoria = Categorias.objects.create(nome="Eletrônicos Edit")
        self.marca = Marca.objects.create(nome="Marca Edit")
        self.modelo = Modelo.objects.create(nome="Modelo Edit", marca=self.marca)

        self.fornecedor_edit = Fornecedor.objects.create(
            nome="Fornecedor Edit Teste",
            contato="Contato Edit Teste",
            endereco="Endereco Edit Teste",
        )

        self.funcao_edit = Funcao.objects.create(nome="Cargo Edit Teste", salario=1500.0)

        self.funcionario_edit = Funcionario.objects.create(
            nome="Funcionario Edit Teste",
            funcao=self.funcao_edit,
            telefone="84888888888",
        )

        self.produto_para_editar = Produtos.objects.create(
            nome="Produto Teste para Editar Entrada",
            fornecedor=self.fornecedor_edit,
            cor="Preto",
            tamanho=8.0,
            modelo=self.modelo,
            marca=self.marca,
            descricao="Um produto para testes de edição de entrada.",
            categoria=self.categoria
        )

        self.entrada_para_editar = Entrada.objects.create(
            quantidade=20,
            valor=3000.00,
            produto=self.produto_para_editar,
            fornecedor=self.fornecedor_edit,
            funcionario=self.funcionario_edit
        )

    def test_editar_entrada_view_post(self):
        print("test_editar_entrada_view_post")
        data_atualizada = {
            "quantidade": 10,
            "valor": 2500.00,
            "produto": self.produto_para_editar.id,
            "fornecedor": self.fornecedor_edit.id,
            "funcionario": self.funcionario_edit.id
        }
        response = self.client.post(
            reverse("editar_entrada", args=[self.entrada_para_editar.id]),
            data=data_atualizada
        )
        self.assertEqual(response.status_code, 302)

        # Verificar se os dados foram atualizados corretamente
        self.entrada_para_editar.refresh_from_db()
        self.assertEqual(self.entrada_para_editar.quantidade, 10)
        self.assertEqual(self.entrada_para_editar.valor, 2500.00)

    def test_editar_entrada_view_post_invalido(self):
        print("test_editar_entrada_view_post_invalido")
        data = {
            "produto": self.produto_para_editar.id,
            "funcionario": self.funcionario_edit.id,
            "valor": -10,  # inválido
            "quantidade": 0  # inválido
        }
        response = self.client.post(
            reverse("editar_entrada", args=[self.entrada_para_editar.id]),
            data
        )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertEqual(Entrada.objects.count(), 1)
