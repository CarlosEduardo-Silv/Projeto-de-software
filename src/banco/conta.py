"""Modelo de domínio inicial do MiniBank (RF04, RF05, RF06, RF08)."""
from datetime import datetime
from decimal import Decimal


class ValorInvalidoError(ValueError):
    """Valor da operação deve ser maior que zero."""


class SaldoInsuficienteError(Exception):
    """Saldo insuficiente para a operação."""


class ContaBloqueadaError(Exception):
    """Conta não está ativa."""


class Conta:
    def __init__(self, numero: str, titular: str, saldo: Decimal = Decimal("0.00")):
        self.numero = numero
        self.titular = titular
        self.saldo = Decimal(saldo)
        self.ativa = True
        self.extrato = []  # lista de (data_hora, tipo, valor, saldo_apos)

    def _validar(self, valor: Decimal) -> Decimal:
        valor = Decimal(valor)
        if valor <= 0:
            raise ValorInvalidoError("O valor deve ser maior que zero.")
        if not self.ativa:
            raise ContaBloqueadaError("Conta bloqueada ou encerrada.")
        return valor

    def _registrar(self, tipo: str, valor: Decimal):
        self.extrato.append((datetime.now(), tipo, valor, self.saldo))

    def depositar(self, valor: Decimal):
        valor = self._validar(valor)
        self.saldo += valor
        self._registrar("DEPOSITO", valor)

    def sacar(self, valor: Decimal):
        valor = self._validar(valor)
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        self.saldo -= valor
        self._registrar("SAQUE", valor)

    def bloquear(self):
        self.ativa = False

    def desbloquear(self):
        self.ativa = True


def transferir(origem: Conta, destino: Conta, valor: Decimal):
    """Transferência atômica: se qualquer etapa falhar, nada é alterado."""
    if origem is destino:
        raise ValueError("Origem e destino devem ser contas distintas.")
    valor = Decimal(valor)
    # valida antes de alterar qualquer saldo
    origem._validar(valor)
    destino._validar(valor)
    if valor > origem.saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")
    origem.saldo -= valor
    origem._registrar("TRANSFERENCIA_ENVIADA", valor)
    destino.saldo += valor
    destino._registrar("TRANSFERENCIA_RECEBIDA", valor)
