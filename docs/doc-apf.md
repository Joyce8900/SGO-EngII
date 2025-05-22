# Análise de Pontos de Função (APF)

A Análise de Pontos de Função (APF) permite medir o tamanho funcional do sistema, considerando as funcionalidades implementadas no projeto de Controle de Estoque e Vendas.

---

## Contagem Indicativa

Na contagem indicativa, considera-se:

- **ALI (Arquivo Lógico Interno)**: 35 PF cada (valor indicativo)
- **AIE (Arquivo de Interface Externa)**: 15 PF cada (valor indicativo)

### Modelo de Dados

```mermaid
erDiagram
    USUARIO ||--o{ GERENTE : "é"
    USUARIO ||--o{ FUNCIONARIO : "é"
    GERENTE ||--o{ FUNCIONARIO : "gerencia"
    GERENTE ||--o{ FORNECEDOR : "cadastra"
    FORNECEDOR ||--o{ PRODUTO : "fornece"
    FUNCIONARIO ||--o{ VENDA : "realiza"
    VENDA ||--o{ ITEM_VENDA : "contém"
    ITEM_VENDA }o--|| PRODUTO : "referencia"
    VENDA ||--|| PAGAMENTO : "processa"
    ESTOQUE ||--|| PRODUTO : "controla"
    CLIENTE ||--o{ VENDA : "efetua"
    PRODUTO ||--o{ CATEGORIA : "pertence a"

    USUARIO {
        int id PK
        string nome
        string login
    }

    GERENTE {
        int usuario_id FK
    }

    FUNCIONARIO {
        int usuario_id FK
    }

    FORNECEDOR {
        int id PK
        string nome
        string contato
    }

    PRODUTO {
        int id PK
        string nome
        decimal preco
        int quantidade
        int fornecedor_id FK
        int categoria_id FK
    }

    CATEGORIA {
        int id PK
        string nome
    }

    ESTOQUE {
        int produto_id PK, FK
        int quantidade_atual
    }

    CLIENTE {
        int id PK
        string nome
        string endereco
        string contato
    }

    VENDA {
        int id PK
        date data
        decimal total
        int funcionario_id FK
        int cliente_id FK
    }

    ITEM_VENDA {
        int venda_id FK
        int produto_id FK
        int quantidade
        decimal subtotal
    }

    PAGAMENTO {
        int id PK
        decimal valor
        string metodo
        string status
        int venda_id FK
    }

# Contagem de Pontos de Função

## Função de Dado, Entidades Relacionadas e Tamanho em PF

| Função de Dado  | Entidades Relacionadas       | Tamanho em PF |
|-----------------|-----------------------------|---------------|
| ALI Produto     | Produto, Categoria, Estoque  | 35 PF         |
| ALI Usuário     | Usuário                     | 35 PF         |
| ALI Cliente     | Cliente, Endereço           | 35 PF         |
| ALI Fornecedor  | Fornecedor                  | 35 PF         |
| ALI Venda       | Venda, Item_Venda           | 35 PF         |

**Total: 175 PF**

---

## Contagem Detalhada

A contagem detalhada considera as Funções de Dados e as Funções de Transação:

- **ALI** (Arquivo Lógico Interno)
- **AIE** (Arquivo de Interface Externa)
- **EE** (Entrada Externa)
- **CE** (Consulta Externa)
- **SE** (Saída Externa)

---

### Explicação dos termos

- **ALR (Arquivos Lógicos Referenciados):** número de arquivos lógicos referenciados pela função.
- **DER (Dados Elementares Referenciados):** número de elementos de dados únicos que a função manipula.
- **SE (Saída Externa):** processos que produzem dados derivados e/ou relatórios formatados.

---

### Tabela de Contagem Detalhada

| Descrição          | Tipo | ALR | DER | Complexidade | Tamanho em PF |
|--------------------|------|-----|-----|--------------|---------------|
| ALI Produto        | ALI  | 3   | 6   | Média        | 10 PF         |
| ALI Usuário        | ALI  | 2   | 4   | Baixa        | 7 PF          |
| ALI Cliente        | ALI  | 2   | 5   | Média        | 10 PF         |
| ALI Fornecedor     | ALI  | 1   | 4   | Baixa        | 7 PF          |
| ALI Venda          | ALI  | 3   | 6   | Média        | 10 PF         |
| Inserir Produto    | EE   | 3   | 5   | Média        | 4 PF          |
| Atualizar Produto  | EE   | 3   | 5   | Média        | 4 PF          |
| Consultar Produto  | CE   | 3   | 5   | Média        | 4 PF          |
| Inserir Usuário    | EE   | 1   | 3   | Baixa        | 3 PF          |
| Atualizar Usuário  | EE   | 1   | 3   | Baixa        | 3 PF          |
| Consultar Usuário  | CE   | 1   | 3   | Baixa        | 3 PF          |
| Inserir Cliente    | EE   | 2   | 4   | Média        | 4 PF          |
| Atualizar Cliente  | EE   | 2   | 4   | Média        | 4 PF          |
| Consultar Cliente  | CE   | 2   | 4   | Média        | 4 PF          |
| Inserir Fornecedor | EE   | 1   | 3   | Baixa        | 3 PF          |
| Atualizar Fornecedor| EE  | 1   | 3   | Baixa        | 3 PF          |
| Consultar Fornecedor| CE  | 1   | 3   | Baixa        | 3 PF          |
| Registrar Venda    | EE   | 3   | 6   | Média        | 4 PF          |
| Consultar Venda    | CE   | 3   | 6   | Média        | 4 PF          |
| Relatório de Vendas| SE   | 2   | 5   | Média        | 5 PF          |

**Total: 98 PF**

