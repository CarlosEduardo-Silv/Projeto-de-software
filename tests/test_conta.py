import sys, os, unittest
from decimal import Decimal
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from banco import (Conta, transferir, SaldoInsuficienteError,
                   ContaBloqueadaError, ValorInvalidoError)


class TestConta(unittest.TestCase):
    def setUp(self):
        self.a = Conta("001", "Ana", Decimal("100.00"))
        self.b = Conta("002", "Bruno", Decimal("50.00"))

    def test_deposito(self):
        self.a.depositar(Decimal("25.50"))
        self.assertEqual(self.a.saldo, Decimal("125.50"))

    def test_saque(self):
        self.a.sacar(Decimal("40"))
        self.assertEqual(self.a.saldo, Decimal("60.00"))

    def test_saque_saldo_insuficiente(self):
        with self.assertRaises(SaldoInsuficienteError):
            self.a.sacar(Decimal("100.01"))
        self.assertEqual(self.a.saldo, Decimal("100.00"))

    def test_valor_invalido(self):
        with self.assertRaises(ValorInvalidoError):
            self.a.depositar(Decimal("0"))

    def test_conta_bloqueada(self):
        self.a.bloquear()
        with self.assertRaises(ContaBloqueadaError):
            self.a.sacar(Decimal("10"))

    def test_transferencia(self):
        transferir(self.a, self.b, Decimal("30"))
        self.assertEqual(self.a.saldo, Decimal("70.00"))
        self.assertEqual(self.b.saldo, Decimal("80.00"))

    def test_transferencia_falha_nao_altera_saldos(self):
        self.b.bloquear()
        with self.assertRaises(ContaBloqueadaError):
            transferir(self.a, self.b, Decimal("30"))
        self.assertEqual(self.a.saldo, Decimal("100.00"))
        self.assertEqual(self.b.saldo, Decimal("50.00"))


if __name__ == "__main__":
    unittest.main()
