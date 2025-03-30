## Descrição do Projeto

O sistema de controle de estoque para ótica tem como objetivo otimizar a gestão do estoque, controlando bem a entrada e a saída de produtos como, por exemplo: armações, lentes e óculos de sol. Esse sistema permite o monitoramento em tempo real do estoque, facilitando muito a organização e também a reposição das mercadorias. Esse sistema também oferece funcionalidades para registrar vendas, acompanhar transações e gerar relatórios detalhados, garantindo uma gestão mais precisa.

Benefícios do Sistema:
-Controle de Estoque em Tempo Real: Monitoramento da disponibilidade dos produtos.


-Gestão de Vendas Eficiente: Registro seguro das transações realizadas.


-Relatórios Detalhados: Emissão de relatórios sobre estoque e vendas.


-Segurança e Acesso Controlado: Definição de permissões conforme o papel do usuário.


-Interface Simples: Facilidade de uso para todos os perfis de usuário.




### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o **Mermaid**.

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
    ESTOQUE ||--o{ PRODUTO : "controla"

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
    }

    ESTOQUE {
        int produto_id FK
        int quantidade_atual
    }

    VENDA {
        int id PK
        date data
        decimal total
        int funcionario_id FK
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
```
