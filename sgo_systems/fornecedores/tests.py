from django.test import TestCase
from django.urls import reverse
from fornecedores.models import Fornecedor

class FornecedorViewsTests(TestCase):
    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste",
            endereco="Rua Central, 123",
            contato="(84) 99999-0000",
            descricao="Fornecedor de roupas"
        )

    def test_fornecedor_create_get(self):
        print("test_fornecedor_create_get")
        response = self.client.get(reverse("fornecedores:fornecedor_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "fornecedores/fornecedor_form.html")

    def test_fornecedor_create_post_valido(self):
        data = {
            "nome": "Fornecedor Novo",
            "endereco": "Rua ABC",
            "contato": "123456789",
            "descricao": "Fornecedor de testes",
        }
        response = self.client.post(reverse("fornecedores:fornecedor_create"), data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Fornecedor.objects.count(), 2)
        novo_fornecedor = Fornecedor.objects.get(nome="Fornecedor Novo")
        self.assertEqual(novo_fornecedor.nome, "Fornecedor Novo")


    def test_fornecedor_create_post_invalido(self):
        print("test_fornecedor_create_post_invalido")
        data = {
            "nome": "",  # obrigatório
            "contato": "",  # obrigatório
            "descricao": "Faltando dados"
        }
        response = self.client.post(reverse("fornecedores:fornecedor_create"), data)
        self.assertEqual(response.status_code, 200)  # Não redireciona
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)
        self.assertIn("contato", form.errors)
        self.assertEqual(Fornecedor.objects.count(), 1)  # Nada salvo

    def test_fornecedor_update_post(self):
        print("test_fornecedor_update_post")
        data = {
            "nome": "Fornecedor Editado",
            "endereco": self.fornecedor.endereco,
            "contato": self.fornecedor.contato,
            "descricao": self.fornecedor.descricao
        }
        response = self.client.post(reverse("fornecedores:fornecedor_update", args=[self.fornecedor.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.fornecedor.refresh_from_db()
        self.assertEqual(self.fornecedor.nome, "Fornecedor Editado")

    def test_fornecedor_delete_post(self):
        print("test_fornecedor_delete_post")
        response = self.client.post(reverse("fornecedores:fornecedor_delete", args=[self.fornecedor.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Fornecedor.objects.count(), 0)

    def test_fornecedor_list_get(self):
        print("test_fornecedor_list_get")
        response = self.client.get(reverse("fornecedores:fornecedor_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "fornecedores/fornecedor_list.html")
        self.assertContains(response, "Fornecedor Teste")

    def test_fornecedor_list_filtrado(self):
        print("test_fornecedor_list_filtrado")
        response = self.client.get(reverse("fornecedores:fornecedor_list"), {
            "nome": "Teste"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fornecedor Teste")
