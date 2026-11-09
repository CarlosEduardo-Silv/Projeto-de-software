# E2 — Revisão dos Requisitos de E1

Requisitos pouco claros foram corrigidos para serem mensuráveis e verificáveis.

| ID | Antes | Depois |
|---|---|---|
| RF05 | "permitir saque, desde que haja saldo suficiente" | "permitir saque de valor > 0 e ≤ saldo disponível (conta corrente) em conta ativa; caso contrário, rejeitar com mensagem de erro" |
| RF06 | "permitir transferência entre contas" | "permitir transferência de valor > 0 entre duas contas ativas distintas, de forma atômica; origem deve ter saldo suficiente" |
| RF07 | "exibir saldo e extrato por período" | "exibir saldo atual e extrato com data, tipo, valor e saldo resultante, filtrado por intervalo de datas, ordenado do mais recente" |
| RF08 | "bloquear, desbloquear e encerrar contas" | "gerente pode bloquear/desbloquear contas; encerramento só com saldo zero. Conta bloqueada não realiza débitos nem créditos" |
| RNF03 | "até 2 s em uso normal" | "95% das consultas de saldo/extrato em ≤ 2 s com até 100 usuários simultâneos" |
| RNF05 | "até 3 telas/passos" | "depósito, saque e transferência concluídos em no máximo 3 passos a partir da tela inicial" |
