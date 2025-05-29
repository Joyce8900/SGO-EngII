# from django.test import TestCase, Client
# from django.urls import reverse
# from produtos.models import Produtos
# from categorias.models import Categorias
# from modelo.models import Modelo
# from marca.models import Marca
# from funcionarios.models import Funcionario
# from fornecedores.models import Fornecedor
# from entrada.models import Entrada

# class EditarEntradaViewTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.categoria = Categorias.objects.create(nome="Eletrônicos Edit")
#         self.marca = Marca.objects.create(nome="Marca Edit")
#         self.modelo = Modelo.objects.create(nome="Modelo Edit", marca=self.marca)

#         self.produto_para_editar = Produtos.objects.create(
#             nome="Produto Teste para Editar Entrada",
#             preco=150.00,
#             quantidade=100, # Quantidade inicial do produto
#             cor="Preto",
#             tamanho=8.0,
#             modelo=self.modelo,
#             marca=self.marca,
#             descricao="Um produto para testes de edição de entrada.",
#             categoria=self.categoria
#         )

#         self.fornecedor_edit = Fornecedor.objects.create(
#             nome="Fornecedor Edit Teste",
#             contato="Contato Edit Teste",
#             endereco="Endereco Edit Teste",
#         )
#         self.funcionario_edit = Funcionario.objects.create(
#             nome="Funcionario Edit Teste",
#             cargo="Cargo Edit Teste",
#             telefone="84888888888",
#         )

#         # Cria uma entrada inicial que será editada nos testes
#         self.entrada_para_editar = Entrada.objects.create(
#             quantidade=20, # Quantidade inicial da entrada
#             valor=3000.00, # 20 * 150 (preço do produto)
#             produto=self.produto_para_editar,
#             fornecedor=self.fornecedor_edit,
#             funcionario=self.funcionario_edit
#         )
        
#         self.produto_para_editar.refresh_from_db()


#     def test_editar_entrada_view_post(self):
#     # Suponha que o produto começa com 100 no estoque
#     self.produto_para_editar.quantidade = 100
#     self.produto_para_editar.save()

#     # Suponha que a entrada original era 20
#     self.entrada_para_editar.quantidade = 20
#     self.entrada_para_editar.save()

#     data_atualizada = {
#         "quantidade": 10,  # nova quantidade da entrada
#         "valor": 3000.00,
#         "produto": self.produto_para_editar.id,
#         "fornecedor": self.fornecedor_edit.id,
#         "funcionario": self.funcionario_edit.id
#     }

#     response = self.client.post(
#         reverse("editar_entrada", args=[self.entrada_para_editar.id]),
#         data=data_atualizada
#     )

#     self.assertEqual(response.status_code, 302)

#     self.produto_para_editar.refresh_from_db()

#     # A diferença é -10 (10 - 20), então 100 - 10 = 90
#     self.assertEqual(self.produto_para_editar.quantidade, 90)

        
#     def test_editar_entrada_view_get(self):
#       print("test_editar_entrada_view_get")
#       ## Teste para o GET da view editar_produto
#       response = self.client.get(reverse("editar_entrada",args=[self.entrada_para_editar.id]))
#       self.assertEqual(response.status_code, 200)
#       self.assertTemplateUsed(response, "editar_entrada.html")
    

#     def test_editar_entrada_view_post_invalido(self):
#       print("test_editar_entrada_view_post_invalido")
#      # Dados inválidos: faltando campos obrigatórios
#       data = {
#            "produto": self.produto_para_editar.id,
           
#            "funcionario": self.funcionario_edit.id,
#            "preco": -10,  
#            "quantidade": 0,  
#           }
#       response = self.client.post(reverse("editar_entrada", args=[self.entrada_para_editar.id]), data)
#       self.assertEqual(response.status_code, 200)
#       form = response.context["form"]
#       self.assertFalse(form.is_valid())
#       self.assertEqual(Entrada.objects.count(), 1)
