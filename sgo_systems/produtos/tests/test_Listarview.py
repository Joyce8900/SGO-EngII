from django.test import TestCase, Client # Garanta Client importado
from django.urls import reverse
from produtos.models import Produtos
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from fornecedores.models import Fornecedor
import uuid
from django.contrib.auth.models import User # Adicione esta importação


class ListarProdutoViewTests(TestCase):
    def setUp(self):
        self.client = Client() # Adicione esta linha
        # Crie um usuário de teste e faça login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword') # Adicione esta linha
        self.client.login(username='testuser', password='testpassword') # Adicione esta linha

        self.categoria = Categorias.objects.create(nome='Categoria Teste')
        self.marca = Marca.objects.create(nome='Marca Teste')
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            contato='Contato Teste',
            endereco='Endereco Teste',
        )
        self.modelo = Modelo.objects.create(nome='Modelo Padrão', marca=self.marca) # Adicionado para garantir que produtos sejam criados com modelo válido
    
    def test_listar_produtos_view(self):
        print("test_listar_produtos_view")
        response = self.client.get(reverse("produtos:listar_produtos")) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_produtos.html") # CORRIGIDO CAMINHO DO TEMPLATE
        self.assertQuerySetEqual(
            response.context["produtos"],
            Produtos.objects.all().order_by("nome"),
            transform=lambda p: p
        )

    def test_listar_produtos_com_termo(self):
        print("test_listar_produtos_com_termo")

        marca = Marca.objects.create(nome='Marca Teste 2')
        modelo = Modelo.objects.create(nome='Modelo Teste 2', marca=marca)
        categoria = Categorias.objects.create(nome='Categoria Teste 2')
        fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste 2',
            contato=f'{uuid.uuid4()}@teste.com',
            endereco='Endereco Teste 2',
        )
        Produtos.objects.create(
            nome='Produto A',
            # REMOVIDO: fornecedor=fornecedor, # <--- Removido este argumento
            categoria=categoria,
            marca=marca,
            descricao='Descrição A',
            tamanho=0.5,
            modelo=modelo,
            quantidade=10, # Adicione quantidade
            preco=10.00, # Adicione preco
        )
        Produtos.objects.create(
            nome='Produto B',
            # REMOVIDO: fornecedor=fornecedor, # <--- Removido este argumento
            categoria=categoria,
            marca=marca,
            descricao='Descrição B',
            tamanho=0.5,
            modelo=modelo,
            quantidade=10, # Adicione quantidade
            preco=10.00, # Adicione preco
        )

        response = self.client.get(reverse('produtos:listar_produtos') + '?termo=Produto A') # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto A')
        self.assertNotContains(response, 'Produto B')

    def test_listar_produto_categoria(self):
        print("test_listar_produto_categoria")

        marca = Marca.objects.create(nome='Marca Teste 3')
        modelo = Modelo.objects.create(nome='Modelo Teste 3', marca=marca)
        categoria1 = Categorias.objects.create(nome='Categoria 1')
        categoria2 = Categorias.objects.create(nome='Categoria 2')
        fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste 3',
            contato=f'{uuid.uuid4()}@teste.com',
            endereco='Endereco Teste 3',
        )

        Produtos.objects.create(
            nome='Produto A',
            # REMOVIDO: fornecedor=fornecedor, # <--- Removido este argumento
            categoria=categoria1,
            marca=marca,
            descricao='Descrição A',
            tamanho=0.5,
            modelo=modelo,
            quantidade=10, # Adicione quantidade
            preco=10.00, # Adicione preco
        )
        Produtos.objects.create(
            nome='Produto B',
            # REMOVIDO: fornecedor=fornecedor, # <--- Removido este argumento
            categoria=categoria2,
            marca=marca,
            descricao='Descrição B',
            tamanho=0.5,
            modelo=modelo,
            quantidade=10, # Adicione quantidade
            preco=10.00, # Adicione preco
        )

        url = reverse('produtos:listar_produtos') + f'?categoria={categoria1.id}' # CORRIGIDO AQUI
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto A')
        self.assertNotContains(response, 'Produto B')

    def test_listar_produtos_sem_produtos(self):
        print("test_listar_produtos_sem_produtos")
        Produtos.objects.all().delete()
        response = self.client.get(reverse('produtos:listar_produtos')) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhum produto encontrado.") # CORRIGIDO AQUI: Mensagem no template