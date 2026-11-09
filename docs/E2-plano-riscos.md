# E2 — Plano do Projeto e Riscos

## Equipe
| Nome | Papel | Responsabilidades |
|---|---|---|
| Carlos Eduardo | Analista / Documentação | Requisitos, UML, README, plano |
 |Yuri veloso | Desenvolvedor | Modelo de domínio, API, testes |

## Recursos
- **Humanos:** dupla de alunos (≈ 6 h/semana cada)
- **Ferramentas:** GitHub (repositório, issues, projects), VS Code, Python, PostgreSQL, Mermaid
- **Ambiente:** computadores pessoais; sem custo financeiro

## Cronograma resumido
| Fase | Atividades | Entrega |
|---|---|---|
| E1 | Problema, requisitos, escopo, repositório | README + requisitos |
| E2 | Arquitetura, UML, plano e riscos | Docs de projeto |
| Implementação | Domínio, API, banco, interface | Sistema funcional |
| Testes | Unitários e de integração | Relatório de testes |
| Entrega | Ajustes e apresentação | Versão final |

## Estratégia de acompanhamento
- Quadro **Kanban** no GitHub Projects (A fazer / Em andamento / Concluído)
- Uma **issue** por requisito (RFxx/RNFxx)
- Reunião semanal de 30 min para revisar progresso e riscos
- Commits pequenos, com mensagens padronizadas (`docs:`, `feat:`, `test:`, `fix:`)
- Revisão cruzada entre os integrantes antes de mesclar alterações

## Riscos
| # | Risco | Prob. | Impacto | Ação preventiva |
|---|---|---|---|---|
| R1 | Escopo crescer (PIX, cartões etc.) | Média | Alto | Manter "fora do escopo" documentado; mudanças só via revisão do escopo |
| R2 | Erros em cálculos financeiros (arredondamento) | Média | Alto | Usar `Decimal`, testes unitários para regras de negócio |
| R3 | Falhas de segurança (senhas, acessos indevidos) | Média | Alto | Hash de senhas, controle de perfis, HTTPS, revisão de segurança |
| R4 | Tempo insuficiente / sobrecarga da dupla | Alta | Médio | Priorizar requisitos de prioridade Alta; acompanhamento semanal |
| R5 | Perda de código/documentação | Baixa | Alto | Repositório Git remoto com commits frequentes |
| R6 | Dificuldade com tecnologias novas | Média | Médio | Protótipos curtos e escolha de tecnologias já conhecidas |
