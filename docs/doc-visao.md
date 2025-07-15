# Sistema de Controle de Estoque para Ótica  

## Descrição do Projeto  
O sistema de controle de estoque para ótica tem como objetivo otimizar a gestão do estoque, controlando a entrada e saída de produtos (armações, lentes, óculos de sol). Oferece:  

- **Controle em tempo real** do estoque  
- **Registro de vendas** e transações  
- **Relatórios detalhados**  
- **Acesso seguro** por perfil de usuário  
- **Interface intuitiva**  

## Equipe  

| Membro            | Papel                   | E-mail                          |
|-------------------|-------------------------|--------------------------------|
| Cayo César        | Analista                | cayo.lopes.129@ufrn.edu.br     |
| Gabriel Gomes     | Analista                | gabriel.gomes.710@ufrn.edu.br  |
| Gustavo Douglas   | Líder Técnico           | gustavo.cruz.133@ufrn.edu.br   |
| Joyce Oliveira    | Analista                | joyce.santos.709@ufrn.edu.br   |
| Taciano Silva     | Cliente/Professor       | tacianosilva@gmail.com          |
| Arthur            | Cliente                 | stegelemon.com.br@gmail.com    |

## Perfis de Usuários  

### Funcionário  
- Visualizar estoque  
- Registrar vendas  
- Emitir comprovantes  

### Gerente  
- Gerenciar produtos, funcionários e fornecedores  
- Acessar relatórios  
- Controlar permissões  

## Requisitos Funcionais

### Entidade Funcionário - US01 - Manter Funcionário

| Código       | Descrição                                                        | Ator    |
|--------------|------------------------------------------------------------------|---------|
| RF01.01      | Inserir Funcionário                                              | Gerente |
| RF01.02      | Listar Funcionários                                              | Gerente |
| RF01.03      | Atualizar Funcionário                                            | Gerente |
| RF01.04      | Deletar Funcionário                                              | Gerente |

---

### Entidade Cliente - US02 - Manter Cliente

| Código       | Descrição                                                        | Ator      |
|--------------|------------------------------------------------------------------|-----------|
| RF02.01      | Inserir Cliente                                                 | Funcionário |
| RF02.02      | Listar Clientes                                                | Funcionário |
| RF02.03      | Atualizar Cliente                                              | Funcionário |
| RF02.04      | Deletar Cliente                                               | Funcionário |

---

### Entidade Fornecedor - US03 - Manter Fornecedor

| Código       | Descrição                                                        | Ator    |
|--------------|------------------------------------------------------------------|---------|
| RF03.01      | Inserir Fornecedor                                              | Gerente |
| RF03.02      | Listar Fornecedores                                            | Gerente |
| RF03.03      | Atualizar Fornecedor                                          | Gerente |
| RF03.04      | Deletar Fornecedor                                            | Gerente |

---

### Entidade Produto - US04 - Manter Produto

| Código       | Descrição                                                        | Ator    |
|--------------|------------------------------------------------------------------|---------|
| RF04.01      | Inserir Produto                                                | Gerente |
| RF04.02      | Listar Produtos                                               | Gerente |
| RF04.03      | Atualizar Produto                                           | Gerente |
| RF04.04      | Deletar Produto                                             | Gerente |

---

### Entidade Entrada de Produto - US05 - Entrar Produto

| Código       | Descrição                                                        | Ator    |
|--------------|------------------------------------------------------------------|---------|
| RF05.01      | Selecionar produto para entrada                               | Gerente |
| RF05.02      | Registrar quantidade e data da entrada                        | Gerente |
| RF05.03      | Associar entrada ao fornecedor                                | Gerente |
| RF05.04      | Validar dados de entrada (quantidade, produto)               | Gerente |
| RF05.05      | Visualizar histórico de entradas                              | Gerente |
| RF05.06      | Filtrar histórico por produto e data                          | Gerente |
| RF05.07      | Cancelar registro de entrada                                  | Gerente |

---

### Entidade Estoque - US06 - Manter Quantidade Em Estoque

| Código       | Descrição                                                        | Ator    |
|--------------|------------------------------------------------------------------|---------|
| RF06.01      | Atualizar estoque na entrada de produtos                      | Sistema |
| RF06.02      | Atualizar estoque na venda                                     | Sistema |
| RF06.03      | Atualizar estoque no cancelamento                              | Sistema |
| RF06.04      | Ajuste manual de estoque                                       | Gerente |

---

### Consulta e Histórico de Estoque - US07 - Visualizar Estoque

| Código       | Descrição                                                        | Ator    |
|--------------|------------------------------------------------------------------|---------|
| RF07.01      | Consultar estoque atual                                        | Funcionário / Gerente |
| RF07.02      | Filtrar por categoria/produto                                 | Funcionário / Gerente |
| RF07.03      | Visualizar histórico de movimentações                         | Gerente |

---

### Relatório de Estoque - US08 - Emitir Relatório de Estoque

| Código       | Descrição                                                        | Ator    |
|--------------|------------------------------------------------------------------|---------|
| RF08.01      | Gerar relatório completo de estoque                            | Gerente |
| RF08.02      | Filtrar relatório por critérios selecionados                   | Gerente |
| RF08.03      | Exibir mensagem de resultado vazio                             | Gerente |
| RF08.04      | Exportar relatório em diferentes formatos                      | Gerente |
| RF08.05      | Cancelar emissão de relatório                                  | Gerente |

---

### Venda - US09 - Realizar Venda

| Código       | Descrição                                                        | Ator        |
|--------------|------------------------------------------------------------------|-------------|
| RF09.01      | Registrar Venda com validação de estoque                      | Funcionário |
| RF09.02      | Emitir Comprovante                                            | Funcionário |
| RF09.03      | Consultar Histórico                                         | Gerente     |
| RF09.04      | Cancelar Venda com reversão de estoque                        | Funcionário |

---

### Pagamento - US10 - Realizar Pagamento

| Código       | Descrição                                                        | Ator        |
|--------------|------------------------------------------------------------------|-------------|
| RF10.01      | Selecionar forma de pagamento                                  | Funcionário / Gerente |
| RF10.02      | Validar dados de pagamento                                     | Funcionário / Gerente |
| RF10.03      | Confirmar pagamento e registrar valor total/parcial            | Funcionário / Gerente |
| RF10.04      | Gerar comprovante de pagamento                                 | Funcionário / Gerente |
| RF10.05      | Cancelar pagamento antes da confirmação                        | Funcionário / Gerente |

---

### Tela Home - US11

| Código       | Descrição                                                        | Ator        |
|--------------|------------------------------------------------------------------|-------------|
| RF11.01      | Exibir menu de navegação principal                             | Todos       |
| RF11.02      | Agrupar funcionalidades por módulos                            | Todos       |
| RF11.03      | Permitir acesso rápido às funções mais utilizadas              | Todos       |
| RF11.04      | Exibir informações resumidas do sistema                        | Todos       |

---

### Funções - US12 - Manter Função

| Código       | Descrição                                                        | Ator        |
|--------------|------------------------------------------------------------------|-------------|
| RF12.01      | Inserir Função                                                | Gerente     |
| RF12.02      | Listar Funções                                               | Gerente     |
| RF12.03      | Atualizar Função                                            | Gerente     |
| RF12.04      | Deletar Função                                             | Gerente     |

---

### Marca - US13 - Manter Marca

| Código       | Descrição                                                        | Ator        |
|--------------|------------------------------------------------------------------|-------------|
| RF13.01      | Inserir Marca                                                 | Gerente     |
| RF13.02      | Listar Marcas                                                | Gerente     |
| RF13.03      | Atualizar Marca                                             | Gerente     |
| RF13.04      | Deletar Marca                                              | Gerente     |

---

### Modelo - US14 - Manter Modelo

| Código       | Descrição                                                        | Ator        |
|--------------|------------------------------------------------------------------|-------------|
| RF14.01      | Inserir Modelo                                                | Gerente     |
| RF14.02      | Listar Modelos                                               | Gerente     |
| RF14.03      | Atualizar Modelo                                            | Gerente     |
| RF14.04      | Deletar Modelo                                             | Gerente     |

---

### Usuários - US15 - Manter Usuário

| Código       | Descrição                                                        | Ator        |
|--------------|------------------------------------------------------------------|-------------|
| RF15.01      | Cadastrar Usuário                                            | Administrador |
| RF15.02      | Autenticar Usuário (Login)                                   | Todos         |
| RF15.03      | Restringir Acesso à Plataforma para usuários autenticados    | Sistema       |

## Requisitos Não Funcionais

| Código  | Requisito       | Descrição                                                                                 | Prioridade   |
|---------|----------------|-------------------------------------------------------------------------------------------|--------------|
| RNF01   | Desempenho     | O sistema deve processar transações e atualizar o estoque em tempo real.                  | Essencial    |
| RNF02   | Segurança      | O sistema deve ter autenticação de usuários e controle de permissões de acesso.           | Essencial    |
| RNF03   | Usabilidade    | O sistema deve ser intuitivo e fácil de usar, com suporte a funcionalidades acessíveis.  | Importante   |
| RNF04   | Confiabilidade | O sistema deve estar disponível durante o horário de funcionamento e possuir backups.     | Essencial    |
