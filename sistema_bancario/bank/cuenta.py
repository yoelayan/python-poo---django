
# Modulo Local
import datetime
from .exceptions import (
    SaldoInsuficienteError
)
from auth.user import Usuario
from .transaction import Transaccion


class Cuenta(Usuario):

    def __init__(
            self,
            nombre: str, email: str,
            password: str, saldo: float = 0.0
            ):
        super().__init__(nombre, email, password)
        self.saldo = saldo
        self.transacciones = []

    def add_transaccion(self, tipo, cantidad):
        self.transacciones.append(
            Transaccion(tipo, cantidad, datetime.now())
        )

    def ver_historico(self):
        for transaccion in self.transacciones:
            print(transaccion)

    def depositar(self, cantidad):
        self.saldo += cantidad
        """
        Podemos realizar una logica, en proyectos reales
        para verificar si la tarjeta usada para depositar
        tiene dinero o no
        """
        self.transacciones.append(
            Transaccion('Deposito', cantidad, datetime.now())
        )
        return f'Ha depositado {cantidad}. El saldo actual de {self.nombre} es {self.saldo}'

    def se_puede_retirar(self, cantidad):
        return cantidad <= self.saldo

    def retirar(self, cantidad):
        if not self.se_puede_retirar(cantidad):
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        return f'Su saldo actual es {self.saldo}'

    def consultar_saldo(self):
        return f'Su saldo actual es {self.saldo}'

    def transferir(self, cuenta_destino, cantidad):
        if not self.se_puede_retirar(cantidad):
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        msg = cuenta_destino.depositar(cantidad)
        return f'Han sido transferidos {cantidad} a {cuenta_destino}', cuenta_destino