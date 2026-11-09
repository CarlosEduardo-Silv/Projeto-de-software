# E2 — Exercícios de Fixação

**Aula 2: Projeto, arquitetura, UML e plano**

## 1. Requisito x projeto
"O sistema deve permitir agendar consultas" é um **requisito**: diz *o que* o sistema deve fazer, do ponto de vista do usuário, sem ditar a tecnologia. "O sistema terá uma interface web, uma API e um banco de dados" é uma decisão de **projeto/arquitetura**: diz *como* o sistema será construído para atender aos requisitos. O requisito é o problema a resolver; o projeto é a forma escolhida de resolvê-lo, e pode mudar sem alterar o requisito.

## 2. UML
- **(a) Atores e funcionalidades → Diagrama de Casos de Uso**, pois mostra quem interage com o sistema e o que cada ator pode fazer.
- **(b) Classes e relacionamentos → Diagrama de Classes**, pois representa a estrutura estática: classes, atributos, métodos, associações e heranças.
- **(c) Sequência de mensagens entre componentes → Diagrama de Sequência**, pois mostra a ordem temporal das interações entre objetos/componentes em um cenário.
- **(d) Fluxo de atividades → Diagrama de Atividades**, pois modela o fluxo de passos, decisões e paralelismos de um processo.

## 3. Arquitetura (sistema de biblioteca)
```
[Interface Web] --> [API / Serviços] --> [Banco de Dados]
                         |
                         +--> [Módulo de Autenticação]
                         +--> [Módulo de Notificações]
```
| Bloco | Responsabilidade |
|---|---|
| Interface Web | Permitir que leitores e bibliotecários busquem livros, façam empréstimos/reservas e vejam seu histórico |
| API / Serviços | Aplicar as regras de negócio (limite de empréstimos, prazos, multas, disponibilidade) |
| Banco de Dados | Armazenar livros, exemplares, usuários, empréstimos e reservas |
| Módulo de Autenticação | Controlar login e permissões (leitor, bibliotecário) |
| Módulo de Notificações | Avisar sobre prazos de devolução, reservas disponíveis e multas |

## 4. Riscos
| Risco | Ação preventiva |
|---|---|
| Requisitos mal compreendidos ou mudando constantemente | Validar requisitos com os usuários e controlar mudanças formalmente |
| Atraso no cronograma por estimativas erradas | Dividir em entregas pequenas e acompanhar o progresso semanalmente |
| Perda de código ou dados do projeto | Usar controle de versão (Git) com repositório remoto e backups |
