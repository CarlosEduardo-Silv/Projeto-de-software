import os, sys, unittest
from datetime import date, timedelta
from decimal import Decimal
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from banco import (Cliente, ContaCorrente, ContaPoupanca, StatusConta, TipoTransacao,
                   SaldoInsuficienteError, ContaBloqueadaError, ContaNaoZeradaError,
                   ValorInvalidoError)


def cliente():
    return Cliente("Ana", "529.982.247-25", "ana@email.com", date(1995, 3, 10))


class TestConta(unittest.TestCase):
    def setUp(self):
        self.cc = ContaCorrente("00001", "0001", cliente(), limite_cheque_especial="100")
        self.cp = ContaPoupanca("00002", "0001", cliente())

    def test_deposito_e_saque(self):
        self.cc.depositar("100.50")
        self.cc.sacar("40")
        self.assertEqual(self.cc.saldo, Decimal("60.50"))

    def test_valores_invalidos(self):
        for v in (0, -5, "abc", "10,5"):
            with self.assertRaises(ValorInvalidoError):
                self.cc.depositar(v)

    def test_cheque_especial_na_corrente(self):
        self.cc.depositar("50")
        self.cc.sacar("150")          # 50 de saldo + 100 de limite
        self.assertEqual(self.cc.saldo, Decimal("-100.00"))
        with self.assertRaises(SaldoInsuficienteError):
            self.cc.sacar("0.01")

    def test_poupanca_sem_cheque_especial(self):
        self.cp.depositar("50")
        with self.assertRaises(SaldoInsuficienteError):
            self.cp.sacar("50.01")

    def test_rendimento_poupanca(self):
        self.cp.depositar("1000")
        t = self.cp.aplicar_rendimento()
        self.assertEqual(t.tipo, TipoTransacao.RENDIMENTO)
        self.assertEqual(self.cp.saldo, Decimal("1005.00"))

    def test_bloqueio_impede_operacoes(self):
        self.cc.depositar("10")
        self.cc.bloquear()
        with self.assertRaises(ContaBloqueadaError):
            self.cc.depositar("1")
        with self.assertRaises(ContaBloqueadaError):
            self.cc.sacar("1")
        self.cc.desbloquear()
        self.cc.sacar("1")

    def test_encerrar_exige_saldo_zero(self):
        self.cc.depositar("10")
        with self.assertRaises(ContaNaoZeradaError):
            self.cc.encerrar()
        self.cc.sacar("10")
        self.cc.encerrar()
        self.assertEqual(self.cc.status, StatusConta.ENCERRADA)
        with self.assertRaises(ContaBloqueadaError):
            self.cc.desbloquear()

    def test_extrato_ordem_e_filtro(self):
        self.cc.depositar("10")
        self.cc.sacar("3")
        extrato = self.cc.extrato_periodo()
        self.assertEqual([t.tipo for t in extrato], [TipoTransacao.SAQUE, TipoTransacao.DEPOSITO])
        self.assertEqual(extrato[0].saldo_apos, Decimal("7.00"))
        amanha = date.today() + timedelta(days=1)
        self.assertEqual(self.cc.extrato_periodo(inicio=amanha), [])


if __name__ == "__main__":
    unittest.main()
