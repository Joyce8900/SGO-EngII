from django.test import TestCase, Client
from django.urls import reverse
from .models import Funcionario
from funcao.models import Funcao
from django.contrib.auth.models import User # Mantenha esta importação

class FuncionarioModelTest(TestCase):
    def setUp(self):
        self.funcao = Funcao.objects.create(nome="Gerente", salario=5000)

    def test_criacao_funcionario(self):
        funcionario = Funcionario.objects.create(
            nome="João Silva",
            funcao=self.funcao,
            telefone="83999998888"
        )
        self.assertEqual(funcionario.nome, "João Silva")
        self.assertEqual(funcionario.funcao, self.funcao)
        self.assertEqual(funcionario.telefone, "83999998888")

class FuncionarioViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Setup de autenticação
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.funcao = Funcao.objects.create(nome="Vendedora", salario=3000)
        self.funcionario = Funcionario.objects.create(
            nome="Maria Souza",
            funcao=self.funcao,
            telefone="83999997777"
        )

    def test_listar_funcionario(self):
        response = self.client.get(reverse('funcionarios:listar_funcionario')) # Corrigido aqui
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maria Souza")

    def test_cadastrar_funcionario(self):
        response = self.client.post(reverse('funcionarios:cadastrar_funcionario'), { # Corrigido aqui
            'nome': 'Carlos Lima',
            'funcao': self.funcao.id,
            'telefone': '83988886666'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Funcionario.objects.filter(nome="Carlos Lima").exists())

    def test_cadastrar_funcionario_sem_funcao(self):
        response = self.client.post(reverse('funcionarios:cadastrar_funcionario'), { # Corrigido aqui
            'nome': 'Sem Funcao',
            'telefone': '83911112222'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Selecione uma função.')

    def test_cadastrar_funcionario_telefone_duplicado(self):
        response = self.client.post(reverse('funcionarios:cadastrar_funcionario'), { # Corrigido aqui
            'nome': 'Repetido',
            'funcao': self.funcao.id,
            'telefone': self.funcionario.telefone
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Telefone já cadastrado.')

    def test_editar_funcionario(self):
        url = reverse('funcionarios:editar_funcionario', args=[self.funcionario.id]) # Corrigido aqui
        response = self.client.post(url, {
            'nome': 'Maria Silva',
            'funcao': self.funcao.id,
            'telefone': '83999997777'
        })
        self.assertEqual(response.status_code, 302)
        self.funcionario.refresh_from_db()
        self.assertEqual(self.funcionario.nome, 'Maria Silva')

    def test_editar_funcionario_sem_funcao(self):
        url = reverse('funcionarios:editar_funcionario', args=[self.funcionario.id]) # Corrigido aqui
        response = self.client.post(url, {
            'nome': 'Maria Editada',
            'telefone': '83999997777',
            # funcao não enviada
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Selecione uma função.')

    def test_editar_funcionario_telefone_duplicado(self):
        outro = Funcionario.objects.create(
            nome="Outro",
            funcao=self.funcao,
            telefone="83912345678"
        )
        url = reverse('funcionarios:editar_funcionario', args=[self.funcionario.id]) # Corrigido aqui
        response = self.client.post(url, {
            'nome': 'Maria',
            'funcao': self.funcao.id,
            'telefone': "83912345678"  # telefone do outro
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Telefone já cadastrado.')

    def test_excluir_funcionario(self):
        url = reverse('funcionarios:deletar_funcionario', args=[self.funcionario.id]) # Corrigido aqui
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Funcionario.objects.filter(id=self.funcionario.id).exists())