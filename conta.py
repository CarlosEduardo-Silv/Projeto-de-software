"""Hierarquia de contas do MiniBank (RF03 a RF08).

Conta é abstrata: ContaCorrente e ContaPoupanca definem apenas quanto do
saldo pode ser usado em débitos; o restante da regra é compartilhado.
"""
from abc import ABC, abstractmethod
from datetime import date, datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN
from enum import Enum
from typing import List, Optional

from .cliente import Cliente
from .excecoes import (ContaBloqueadaError, ContaNaoZeradaError,
                       SaldoInsuficienteError, ValorInvalidoError)
from .transacao import TipoTransacao, Transacao

CENTAVO = Decimal("0.01")


def para_decimal(valor) -> Decimal:
    """Converte para Decimal com 2 casas (nunca usar float para dinheiro)."""
    try:
        return Decimal(str(valor)).quantize(CENTAVO, rounding=ROUND_HALF_EVEN)
    except (InvalidOperation, ValueError):
        raise ValorInvalidoError("Valor inválido.")


class StatusConta(Enum):
    ATIVA = "ATIVA"
    BLOQUEADA = "BLOQUEADA"
    ENCERRADA = "ENCERRADA"


class Conta(ABC):
    tipo = "CONTA"

    def __init__(self, numero: str, agencia: str, titular: Cliente):
        self.numero = numero
        self.agencia = agencia
        self.titular = titular
        self.status = StatusConta.ATIVA
        self._saldo = Decimal("0.00")
        self._transacoes: List[Transacao] = []

    @property
    def saldo(self) -> Decimal:
        return self._saldo

    @abstractmethod
    def saldo_disponivel(self) -> Decimal:
        """Quanto pode ser debitado agora."""

    # ---- validações (usadas também pelo Banco para transferências atômicas)
    def validar_credito(self, valor) -> Decimal:
        valor = para_decimal(valor)
        if valor <= 0:
            raise ValorInvalidoError("O valor deve ser maior que zero.")
        if self.status != StatusConta.ATIVA:
            raise ContaBloqueadaError(f"Conta {self.status.value.lower()}.")
        return valor

    def validar_debito(self, valor) -> Decimal:
        valor = self.validar_credito(valor)
        if valor > self.saldo_disponivel():
            raise SaldoInsuficienteError("Saldo insuficiente.")
        return valor

    # ---- movimentações de baixo nível (valor já validado)
    def creditar(self, valor: Decimal, tipo: TipoTransacao,
                 contraparte: Optional[str] = None) -> Transacao:
        self._saldo += valor
        return self._registrar(tipo, valor, contraparte)

    def debitar(self, valor: Decimal, tipo: TipoTransacao,
                contraparte: Optional[str] = None) -> Transacao:
        self._saldo -= valor
        return self._registrar(tipo, valor, contraparte)

    def _registrar(self, tipo, valor, contraparte) -> Transacao:
        t = Transacao(tipo, valor, self._saldo, datetime.now(), contraparte)
        self._transacoes.append(t)
        return t

    # ---- operações públicas
    def depositar(self, valor) -> Transacao:
        return self.creditar(self.validar_credito(valor), TipoTransacao.DEPOSITO)

    def sacar(self, valor) -> Transacao:
        return self.debitar(self.validar_debito(valor), TipoTransacao.SAQUE)

    def extrato_periodo(self, inicio: Optional[date] = None,
                        fim: Optional[date] = None) -> List[Transacao]:
        """Extrato do mais recente para o mais antigo, filtrado por datas."""
        itens = [t for t in self._transacoes
                 if (inicio is None or t.data_hora.date() >= inicio)
                 and (fim is None or t.data_hora.date() <= fim)]
        return list(reversed(itens))

    def bloquear(self):
        self._exigir_nao_encerrada()
        self.status = StatusConta.BLOQUEADA

    def desbloquear(self):
        self._exigir_nao_encerrada()
        self.status = StatusConta.ATIVA

    def encerrar(self):
        if self._saldo != 0:
            raise ContaNaoZeradaError("Só é possível encerrar conta com saldo zero.")
        self.status = StatusConta.ENCERRADA

    def _exigir_nao_encerrada(self):
        if self.status == StatusConta.ENCERRADA:
            raise ContaBloqueadaError("Conta encerrada.")

    def __str__(self) -> str:
        return (f"{self.tipo} {self.agencia}/{self.numero} - {self.titular.nome} "
                f"[{self.status.value}] saldo R$ {self._saldo}")


class ContaCorrente(Conta):
    tipo = "CORRENTE"

    def __init__(self, numero, agencia, titular,
                 limite_cheque_especial=Decimal("0.00")):
        super().__init__(numero, agencia, titular)
        self.limite_cheque_especial = para_decimal(limite_cheque_especial)

    def saldo_disponivel(self) -> Decimal:
        return self._saldo + self.limite_cheque_especial


class ContaPoupanca(Conta):
    tipo = "POUPANÇA"

    def __init__(self, numero, agencia, titular, taxa_rendimento=Decimal("0.005")):
        super().__init__(numero, agencia, titular)
        self.taxa_rendimento = Decimal(str(taxa_rendimento))

    def saldo_disponivel(self) -> Decimal:
        return self._saldo  # poupança não tem cheque especial

    def aplicar_rendimento(self) -> Optional[Transacao]:
        """Credita o rendimento do período (chamada manual nesta versão)."""
        valor = (self._saldo * self.taxa_rendimento).quantize(CENTAVO)
        if valor <= 0:
            return None
        valor = self.validar_credito(valor)
        return self.creditar(valor, TipoTransacao.RENDIMENTO)
