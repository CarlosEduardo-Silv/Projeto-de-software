# E1 — Requisitos e Escopo: MiniBank

## 1. Tema
Sistema bancário digital de pequeno porte.

## 2. Problema
Em instituições financeiras pequenas, o controle de contas e movimentações costuma ser feito por planilhas, papéis e atendimento presencial. Isso gera registros dispersos e sem histórico confiável, divergências de saldo por erros de lançamento manual, demora na execução de operações como transferências, impossibilidade de o cliente consultar saldo e extrato sem ir à agência e dificuldade de rastrear quem fez cada alteração. Falta uma forma organizada, segura e auditável de registrar clientes, contas e movimentações.

## 3. Usuários / Stakeholders
| Stakeholder | Interesse |
|---|---|
| Cliente | Consultar saldo/extrato e movimentar dinheiro com segurança e rapidez |
| Gerente | Cadastrar clientes e administrar contas sem retrabalho |
| Administrador | Gerenciar acessos e auditar operações |
| Instituição (dona do negócio) | Reduzir erros, fraudes e custo operacional |
| Órgãos reguladores / auditoria | Rastreabilidade e conformidade das operações |
| Equipe de desenvolvimento | Requisitos claros e escopo controlado |

## 4. Requisitos Funcionais
| ID | Requisito | Prioridade |
|---|---|---|
| RF01 | O sistema deve permitir cadastrar clientes (nome, CPF, e-mail, data de nascimento) | Alta |
| RF02 | O sistema deve autenticar usuários por CPF/e-mail e senha | Alta |
| RF03 | O sistema deve permitir abrir conta corrente ou poupança para um cliente cadastrado | Alta |
| RF04 | O sistema deve permitir depósito em uma conta | Alta |
| RF05 | O sistema deve permitir saque, desde que haja saldo suficiente | Alta |
| RF06 | O sistema deve permitir transferência entre contas, debitando a origem e creditando o destino | Alta |
| RF07 | O sistema deve exibir saldo e extrato por período | Média |
| RF08 | O sistema deve permitir ao gerente bloquear, desbloquear e encerrar contas | Média |

## 5. Requisitos Não Funcionais
| ID | Categoria | Requisito |
|---|---|---|
| RNF01 | Segurança | Senhas armazenadas com hash e comunicação via HTTPS |
| RNF02 | Integridade | Operações financeiras atômicas (transferência completa ou nada); valores em tipo decimal |
| RNF03 | Desempenho | Consultas de saldo/extrato respondem em até 2 s em uso normal |
| RNF04 | Auditabilidade | Toda operação registra usuário, data/hora, tipo e valor |
| RNF05 | Usabilidade | Operações principais em até 3 telas/passos |
| RNF06 | Manutenibilidade | Código modularizado, com testes automatizados nas regras de negócio |

## 6. Escopo Inicial
**Dentro do escopo**
- Cadastro de clientes, autenticação e perfis (cliente, gerente, administrador)
- Contas corrente e poupança
- Depósito, saque e transferência entre contas do próprio banco
- Saldo e extrato
- Bloqueio/encerramento de contas
- Auditoria básica das operações

**Fora do escopo (nesta versão)**
- Integração com outros bancos (TED/DOC/PIX real)
- Cartões de crédito/débito, empréstimos e financiamentos
- Investimentos e rendimento automático da poupança
- Aplicativo mobile nativo
- Integração com órgãos reguladores (ex.: Banco Central)
- Detecção de fraude com IA

