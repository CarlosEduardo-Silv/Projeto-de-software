"""Cliente do banco (RF01)."""
from dataclasses import dataclass
from datetime import date

from .excecoes import ClienteInvalidoError


def validar_cpf(cpf: str) -> str:
    """Valida o CPF (dígitos verificadores) e devolve só os 11 dígitos."""
    digitos = "".join(c for c in str(cpf) if c.isdigit())
    if len(digitos) != 11 or digitos == digitos[0] * 11:
        raise ClienteInvalidoError("CPF inválido.")
    for tamanho in (9, 10):
        soma = sum(int(digitos[i]) * (tamanho + 1 - i) for i in range(tamanho))
        dv = (soma * 10) % 11 % 10
        if dv != int(digitos[tamanho]):
            raise ClienteInvalidoError("CPF inválido.")
    return digitos


@dataclass
class Cliente:
    nome: str
    cpf: str
    email: str
    data_nascimento: date

    def __post_init__(self):
        self.nome = self.nome.strip()
        if not self.nome:
            raise ClienteInvalidoError("Nome é obrigatório.")
        self.cpf = validar_cpf(self.cpf)
        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            raise ClienteInvalidoError("E-mail inválido.")
        if self.data_nascimento > date.today():
            raise ClienteInvalidoError("Data de nascimento no futuro.")

    def cpf_formatado(self) -> str:
        c = self.cpf
        return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"
