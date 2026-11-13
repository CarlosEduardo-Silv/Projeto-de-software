"""Registro imutável de uma movimentação (entrada do extrato)."""
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional


class TipoTransacao(Enum):
    DEPOSITO = "DEPÓSITO"
    SAQUE = "SAQUE"
    TRANSFERENCIA_ENVIADA = "TRANSFERÊNCIA ENVIADA"
    TRANSFERENCIA_RECEBIDA = "TRANSFERÊNCIA RECEBIDA"
    RENDIMENTO = "RENDIMENTO"


@dataclass(frozen=True)
class Transacao:
    tipo: TipoTransacao
    valor: Decimal
    saldo_apos: Decimal
    data_hora: datetime
    contraparte: Optional[str] = None  # número da outra conta, em transferências

    def __str__(self) -> str:
        extra = f" (conta {self.contraparte})" if self.contraparte else ""
        return (f"{self.data_hora:%d/%m/%Y %H:%M}  {self.tipo.value:<24} "
                f"R$ {self.valor:>10}  saldo R$ {self.saldo_apos:>10}{extra}")
