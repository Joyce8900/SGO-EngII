# SGO - Sistema de Gerenciamento de Ótica

Este repositório é destinado ao desenvolvimento de um Sistema de Gerenciamento de Ótica, elaborado como parte da disciplina de **Engenharia de Software II**.

---

## Tecnologias Utilizadas

- [Django (Python)](https://www.djangoproject.com/)

---

## Documentação

- [Documento de Visão](docs/doc-visao.md)  
- [User Stories](docs/doc-userstories.md)  
- [Plano de Iteração](docs/doc-plano-de-iteracao.md)  
- [Arquitetura](docs/doc-arquitetura.md)  

---

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto localmente:

### 1. Crie e ative um ambiente virtual

```bash
python -m venv venv
```

**Ative o ambiente virtual:**

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/MacOS**:
  ```bash
  source venv/bin/activate
  ```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure variáveis de ambiente

- Gere uma chave secreta (SECRET_KEY):

  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```

- Crie um arquivo `.env` na raiz do projeto com o conteúdo do `.env.example`, preenchendo os seguintes campos:

```env
SECRET_KEY='sua-secret-key-gerada'
DEBUG=True  # ou False
POSTGRES_DB=nome_do_banco
POSTGRES_USER=usuario
POSTGRES_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432
```

### 4. Prepare o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

Abra o navegador e acesse:

```
http://localhost:8000
```
