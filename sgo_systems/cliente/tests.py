from django.test import TestCase
from django.urls import reverse
from cliente.models import Cliente
from django.contrib.auth.models import User # <--- Adicione esta importação

class ClienteViewsTests(TestCase):
    def setUp(self):
        # Cria um usuário de teste e faz login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword') # <--- Adicione esta linha

        self.cliente = Cliente.objects.create(
            nome="Cliente Teste",
            cpf="12345678900",
            contato="(84) 99999-0000",
            endereco="Rua Central, 123"
        )

    def test_cliente_novo_get(self):
        print("test_cliente_novo_get")
        response = self.client.get(reverse("clientes:cliente_novo"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cliente_form.html")

    def test_cliente_novo_post_valido(self):
        data = {
            "nome": "Cliente Novo",
            "cpf": "98765432100",
            "contato": "11999999999",
            "endereco": "Rua Nova, 456",
        }
        response = self.client.post(reverse("clientes:cliente_novo"), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cliente.objects.count(), 2)
        novo_cliente = Cliente.objects.get(nome="Cliente Novo")
        self.assertEqual(novo_cliente.cpf, "98765432100")

    def test_cliente_novo_post_invalido(self):
        print("test_cliente_novo_post_invalido")
        data = {
            "nome": "",  # obrigatório
            "cpf": "",   # obrigatório
            "contato": "11999999999",
            "endereco": "Rua sem nome"
        }
        response = self.client.post(reverse("clientes:cliente_novo"), data)
        self.assertEqual(response.status_code, 200)  # Não redireciona
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)
        self.assertIn("cpf", form.errors)
        self.assertEqual(Cliente.objects.count(), 1)  # Nada salvo

    def test_cliente_update_post(self):
        print("test_cliente_update_post")
        data = {
            "nome": "Cliente Editado",
            "cpf": self.cliente.cpf,
            "contato": self.cliente.contato,
            "endereco": self.cliente.endereco
        }
        response = self.client.post(reverse("clientes:cliente_update", args=[self.cliente.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nome, "Cliente Editado")

    def test_cliente_delete_post(self):
        print("test_cliente_delete_post")
        response = self.client.post(reverse("clientes:cliente_delete", args=[self.cliente.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cliente.objects.count(), 0)

    def test_cliente_list_get(self):
        print("test_cliente_list_get")
        response = self.client.get(reverse("clientes:cliente_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cliente_list.html")
        self.assertContains(response, "Cliente Teste")

    def test_cliente_list_filtrado(self):
        print("test_cliente_list_filtrado")
        response = self.client.get(reverse("clientes:cliente_list"), {
            "nome": "Teste"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cliente Teste")
