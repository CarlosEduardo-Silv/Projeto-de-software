"""Interface de linha de comando do MiniBank (primeiro incremento).

Uso (a partir da pasta src/):
    python -m banco          # menu interativo
    python -m banco --demo   # cenário de demonstração automático
"""
import sys
from datetime import datetime
from decimal import Decimal

from .banco import Banco
from .excecoes import BancoError

MENU = """
===== MiniBank =====
1) Cadastrar cliente        6) Consultar saldo
2) Abrir conta              7) Ver extrato
3) Depositar                8) Bloquear/desbloquear conta
4) Sacar                    9) Encerrar conta
5) Transferir               0) Sair
"""


def _data(texto: str):
    return datetime.strptime(texto.strip(), "%d/%m/%Y").date()


def _valor(texto: str):
    return texto.strip().replace(",", ".")


def _mostrar_extrato(itens):
    if not itens:
        print("  (sem movimentações)")
    for t in itens:
        print("  " + str(t))


def demo():
    banco = Banco()
    print(">> Cadastrando clientes e abrindo contas")
    ana = banco.cadastrar_cliente("Ana Souza", "529.982.247-25", "ana@email.com", _data("10/03/1995"))
    bruno = banco.cadastrar_cliente("Bruno Lima", "111.444.777-35", "bruno@email.com", _data("22/07/1990"))
    cc = banco.abrir_conta(ana.cpf, "corrente", limite_cheque_especial=Decimal("200"))
    cp = banco.abrir_conta(bruno.cpf, "poupanca")
    print("  ", cc, "\n  ", cp)

    print("\n>> Depósito de 1000,00 e saque de 150,00 na conta de Ana")
    banco.depositar(cc.numero, "1000.00")
    banco.sacar(cc.numero, "150.00")
    print("  saldo:", cc.saldo)

    print("\n>> Transferência de 300,00 de Ana para Bruno")
    banco.transferir(cc.numero, cp.numero, "300.00")
    print("  saldo Ana:", cc.saldo, "| saldo Bruno:", cp.saldo)

    print("\n>> Saque de 1000,00 (saldo 550 + limite 200 = 750: deve falhar)")
    try:
        banco.sacar(cc.numero, "1000.00")
    except BancoError as erro:
        print("  Erro esperado:", erro)

    print("\n>> Bloqueando a conta de Bruno e tentando depositar")
    banco.bloquear_conta(cp.numero)
    try:
        banco.depositar(cp.numero, "50")
    except BancoError as erro:
        print("  Erro esperado:", erro)

    print("\n>> Extrato da conta de Ana")
    _mostrar_extrato(banco.extrato(cc.numero))
    return 0


def interativo():
    banco = Banco()
    while True:
        print(MENU)
        op = input("Opção: ").strip()
        try:
            if op == "1":
                c = banco.cadastrar_cliente(input("Nome: "), input("CPF: "), input("E-mail: "),
                                            _data(input("Nascimento (dd/mm/aaaa): ")))
                print("Cliente cadastrado:", c.nome, c.cpf_formatado())
            elif op == "2":
                tipo = input("Tipo (corrente/poupanca): ").strip()
                extra = {}
                if tipo.lower() == "corrente":
                    extra["limite_cheque_especial"] = _valor(input("Limite do cheque especial [0]: ") or "0")
                print("Conta aberta:", banco.abrir_conta(input("CPF do titular: "), tipo, **extra))
            elif op == "3":
                t = banco.depositar(input("Conta: ").strip(), _valor(input("Valor: ")))
                print("OK:", t)
            elif op == "4":
                t = banco.sacar(input("Conta: ").strip(), _valor(input("Valor: ")))
                print("OK:", t)
            elif op == "5":
                saida, _ = banco.transferir(input("Conta origem: ").strip(),
                                            input("Conta destino: ").strip(), _valor(input("Valor: ")))
                print("OK:", saida)
            elif op == "6":
                print(banco.buscar_conta(input("Conta: ").strip()))
            elif op == "7":
                ini, fim = input("Início (dd/mm/aaaa, opcional): "), input("Fim (dd/mm/aaaa, opcional): ")
                _mostrar_extrato(banco.extrato(input("Conta: ").strip(),
                                               _data(ini) if ini else None, _data(fim) if fim else None))
            elif op == "8":
                numero = input("Conta: ").strip()
                if input("(b)loquear ou (d)esbloquear? ").lower().startswith("b"):
                    banco.bloquear_conta(numero)
                else:
                    banco.desbloquear_conta(numero)
                print(banco.buscar_conta(numero))
            elif op == "9":
                banco.encerrar_conta(input("Conta: ").strip())
                print("Conta encerrada.")
            elif op == "0":
                return 0
            else:
                print("Opção inválida.")
        except BancoError as erro:
            print("Erro:", erro)
        except ValueError:
            print("Erro: data em formato inválido (use dd/mm/aaaa).")


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    return demo() if "--demo" in argv else interativo()
