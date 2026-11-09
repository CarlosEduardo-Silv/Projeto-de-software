# E1 — Exercícios de Fixação

**Aula 1: Engenharia de Software, requisitos e ciclo de vida**

## 1. Situação-problema
Iniciar direto pela programação não basta porque ainda não se sabe exatamente *o que* precisa ser resolvido: quais informações da oficina devem ser registradas, quem usa o sistema, o que significa "status do veículo" e quais etapas do atendimento existem. Sem levantar necessidades e planejar, o programa pode automatizar o processo errado, repetir o retrabalho e perder o histórico de novo. É preciso entender o problema, definir requisitos, projetar a solução, testar e planejar a manutenção, para que o resultado seja organizado, verificável e útil.

## 2. Ciclo de vida
Sequência coerente:
1. **Levantamento de necessidades** — entender o problema e o que os usuários precisam, registrando os requisitos.
2. **Projeto** — definir como o sistema será estruturado (arquitetura, dados, interfaces) para atender aos requisitos.
3. **Implementação** — transformar o projeto em código funcionando.
4. **Testes** — verificar se o sistema atende aos requisitos e encontrar defeitos antes da entrega.
5. **Manutenção/evolução** — corrigir erros e adaptar o sistema a novas necessidades depois de entregue.

## 3. Requisitos (sistema da oficina)
**Funcionais**
- RF1: O sistema deve permitir registrar um serviço associado a um veículo e cliente, com data e descrição.
- RF2: O sistema deve permitir consultar e atualizar o status do veículo (aguardando, em manutenção, pronto, entregue).

**Não funcionais**
- RNF1: O histórico de serviços deve ser mantido de forma persistente, sem perda de dados (confiabilidade).
- RNF2: O atendente deve conseguir consultar o status de um veículo em até 3 cliques/2 segundos (usabilidade/desempenho).

## 4. Análise crítica
O **problema do usuário** é a dificuldade ou necessidade real vivida por quem usa o sistema (ex.: "o cliente liga e ninguém sabe se o carro está pronto"). A **solução de software** é o meio técnico para resolvê-lo (ex.: aplicativo, banco de dados, API). O problema existe independentemente da tecnologia; a solução é uma das respostas possíveis.

*Exemplo:* um banco decide "vamos fazer um aplicativo mobile" antes de analisar o problema. Depois descobre que o principal incômodo dos clientes idosos era a fila e a falta de extrato impresso/consulta simples. O aplicativo seria uma escolha inadequada; um canal web simples ou atendimento assistido resolveria melhor e custaria menos.
