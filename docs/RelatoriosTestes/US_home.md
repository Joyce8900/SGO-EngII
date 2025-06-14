### User Story US11 - Tela Home (Dashboard)

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | Como usuário do sistema, quero acessar uma tela inicial que mostre de forma organizada e intuitiva todas as rotas/funcionalidades disponíveis, para poder navegar eficientemente pelo sistema. |

| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **TA11.01** | **Acesso às rotas principais:** A tela deve exibir claramente os módulos: Cadastros, Estoque, Vendas e Relatórios, com ícones intuitivos. |
| **TA11.02** | **Navegação eficiente:** Cada item do menu deve redirecionar corretamente para a tela correspondente em até 2 cliques. |
| **TA11.03** | **Layout responsivo:** A tela deve se adaptar corretamente em desktop (1440px) e mobile (360px). |
| **TA11.04** | **Atalhos visíveis:** Deve exibir os 5 processos mais utilizados (ex: Nova Venda, Consultar Estoque) com destaque. |
| **TA11.05** | **Informações contextuais:** Deve mostrar resumo do dia (total de vendas, alertas de estoque baixo) quando aplicável. |
| **TA11.06** | **Personalização:** O gerente pode reorganizar os atalhos principais conforme necessidade. |

## Relatório de Testes de Módulo/Sistema  
**Responsabilidade do Testador**

---

### US011 – Tela Home (Dashboard)

| **Teste** | **Descrição** | **Especificação** | **Resultado** |
|----------|---------------|-------------------|---------------|
| **Teste 01: Exibição dos módulos principais** | TA11.01 – Acesso às rotas principais  <br> O ator acessa a tela inicial. <br> O sistema deve exibir claramente os módulos: Cadastros, Estoque, Vendas e Relatórios com ícones intuitivos. | Os módulos são exibidos conforme descrito. Os ícones estão visíveis e correspondem às funções. | OK. ✅ |
| **Teste 02: Navegação entre módulos** | TA11.02 – Navegação eficiente  <br> O ator clica em cada item do menu lateral. <br> O sistema redireciona corretamente para as respectivas telas em até 2 cliques. | A navegação ocorre corretamente e sem travamentos. | OK. ✅ |
| **Teste 03: Responsividade da interface** | TA11.03 – Layout responsivo  <br> O sistema é testado em resoluções 1440px (desktop) e 360px (mobile). | O layout se adapta bem nos dois tamanhos. Nenhum componente se sobrepôs. | OK. ✅ |
| **Teste 04: Atalhos visíveis na Home** | TA11.04 – Atalhos visíveis  <br> A tela exibe atalhos para os 5 processos mais utilizados, como Nova Venda e Consultar Estoque. | São exibidos todos os atalhos das funções atualmente implementadas | OK. ✅ |
| **Teste 05: Informações resumidas** | TA11.05 – Informações contextuais  <br> Ao acessar a tela, o sistema deve exibir total de vendas do dia e alertas de estoque baixo. | Ainda não foi estoque nem vendas, mas é interessante ter um layout com dados simulados enquanto isso. | Incompleto. ⚠️ |
| **Teste 06: Personalização dos atalhos** | TA11.06 – Personalização de atalhos  <br> O gerente arrasta e reorganiza os atalhos conforme sua preferência. <br> A nova ordem é mantida na próxima sessão. | A personalização ainda não foi implementada. | Falha. ❌ |

---

## Relatório de Bugs e Providências  
**Responsabilidade do Gerente**

| **Teste** | **Providência** | **Tarefas/Tipo** |
|----------|------------------|------------------|
| Teste 05 – Informações resumidas | Implementar layout com dados simulados de vendas e alertas, enquanto o módulo real não está disponível. | Tarefa: Implementação parcial. |
| Teste 06 – Personalização dos atalhos | Implementar funcionalidade de personalização descrita no TA11.06. | Tarefa: Funcionalidade não implementada. |
