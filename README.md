# MiniBank — Sistema Bancário

Projeto Integrador da disciplina **Projeto de Software** (UFBRA) — Professor: Jefferson Brandão.

## Objetivo
Desenvolver um sistema bancário digital de pequeno porte que permita a clientes abrir contas e realizar operações financeiras básicas (depósito, saque, transferência, saldo e extrato) com segurança, rastreabilidade e consistência dos dados.

## Usuários
- **Cliente:** titular de conta que consulta saldo/extrato e realiza operações.
- **Gerente:** funcionário que cadastra clientes, abre/bloqueia/encerra contas.
- **Administrador:** gerencia usuários do sistema e consulta auditoria.

## Funcionalidades iniciais
- Cadastro de clientes e autenticação (login)
- Abertura de conta (corrente e poupança)
- Depósito, saque e transferência entre contas
- Consulta de saldo e extrato
- Bloqueio e encerramento de contas (gerente)
- Registro de auditoria das operações

## Equipe
| Nome | Papel |
|------|-------|
| Carlos Eduardo | Analista de requisitos / Documentação |
| Yuri Veloso | Desenvolvedor / Modelagem |

## Estrutura do repositório
```
docs/   documentação (requisitos, arquitetura, UML, plano, riscos, exercícios)
src/    código-fonte (modelo de domínio inicial)
tests/  testes automatizados
```

## Documentação
- [E1 — Requisitos e escopo](docs/E1-requisitos-escopo.md)
- [E1 — Exercícios de fixação](docs/E1-exercicios-fixacao.md)
- [E2 — Revisão dos requisitos](docs/E2-revisao-requisitos.md)
- [E2 — Arquitetura, interfaces e dados](docs/E2-arquitetura.md)
- [E2 — Diagramas UML](docs/E2-diagramas-uml.md) (casos de uso, classes, sequência, atividades)
- [E2 — Plano, equipe, recursos e riscos](docs/E2-plano-riscos.md)
- [E2 — Exercícios de fixação](docs/E2-exercicios-fixacao.md)

## Como executar os testes
```bash
python -m unittest discover -s tests -v
```
