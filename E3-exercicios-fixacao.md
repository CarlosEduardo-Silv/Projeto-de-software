# E3 — Exercícios de Fixação

**Aula 3: Análise orientada a objetos, manutenção e primeiro incremento**

## 1. Classe x objeto
Uma **classe** é o molde que define quais atributos e operações os elementos de um tipo terão; um **objeto** é uma instância concreta desse molde, com valores próprios. Exemplo: a classe `Smartphone` define `modelo`, `bateria` e a operação `ligar()`. Os objetos são o smartphone da Maria (modelo "X10", bateria 80%) e o do João (modelo "Z5", bateria 35%). Ambos seguem a mesma classe, mas têm estados diferentes.

## 2. Modelagem OO (empréstimo de equipamentos)
| Classe | Atributos | Operação |
|---|---|---|
| Equipamento | codigo, descricao, estado | marcarComoEmprestado() |
| Solicitante | nome, matricula | solicitarEmprestimo(equipamento) |
| Emprestimo | dataRetirada, dataPrevistaDevolucao | registrarDevolucao() |
| Atendente | nome, login | registrarEmprestimo(solicitante, equipamento) |

## 3. Relacionamentos
**Solicitante 1 — 0..\* Emprestimo** (associação). Um solicitante pode fazer vários empréstimos ao longo do tempo, mas cada empréstimo pertence a um único solicitante. Isso permite consultar o histórico de quem pegou o quê e controlar atrasos. Do mesmo modo, cada Emprestimo se associa a um Equipamento, e um equipamento só pode estar em um empréstimo aberto por vez.

## 4. Manutenção
- **(a) Corrigir cálculo errado → Corretiva.** Elimina um defeito que já se manifestou.
- **(b) Adaptar a nova API → Adaptativa.** O sistema precisa se ajustar a uma mudança no ambiente externo, sem mudar o que ele faz para o usuário.
- **(c) Adicionar exportação em PDF → Perfectiva/evolutiva.** Acrescenta uma funcionalidade nova ou melhora o sistema a pedido do usuário.
- **(d) Refatorar trecho difícil de manter antes de ocorrer um erro → Preventiva.** Melhora a estrutura interna para evitar problemas futuros, sem mudar o comportamento.
