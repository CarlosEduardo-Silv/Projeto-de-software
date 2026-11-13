# Marco Intermediário — MiniBank

**Data:** 12/11/2026

## Entregue até agora
- **E1:** problema, stakeholders, requisitos e escopo.
- **E2:** arquitetura em 5 blocos, diagramas UML, interfaces, plano e riscos.
- **E3:** modelo OO com 6 classes, diagrama de classes e primeiro incremento funcional com 20 testes e CLI.

## Situação dos requisitos
| Requisito | Situação |
|---|---|
| RF01, RF03, RF04, RF05, RF06, RF07, RF08 | Implementados no domínio e acessíveis pela CLI |
| RF02 Autenticação | Pendente |
| RNF01 Segurança (hash de senhas, HTTPS) | Pendente |
| RNF02 Integridade | Atendido (Decimal e transferência atômica) |
| RNF04 Auditoria | Parcial: transações registradas; falta registrar usuário/ação |
| RNF06 Testes | Atendido para o domínio |

## Riscos revistos
- **R1 (escopo):** controlado; PIX e cartões continuam fora do escopo.
- **R2 (cálculos):** mitigado com `Decimal` e testes.
- **R4 (tempo):** autenticação e persistência ainda pendentes; priorizar.

## Próximos passos
1. Persistência dos dados (arquivo/SQLite ou PostgreSQL).
2. Perfis, autenticação e auditoria (RF02, RNF01, RNF04).
3. API REST conforme `docs/E2-arquitetura.md`.
4. Interface web e testes de integração.
