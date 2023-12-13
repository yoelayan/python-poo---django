
# Modulo Local
from datetime import datetime

from .exceptions import (
    InvalidoError,
    SaldoInsuficienteError
)
from auth.user import Usuario
from .transaction import Transaccion


class Cuenta(Usuario):
    saldo: float = 0.0

    def __init__(self, *args, **kwargs):
        self.transacciones: list = []
        super().__init__(*args, **kwargs)

    def add_transaccion(self, tipo, cantidad):
        self.transacciones.append(
            Transaccion(tipo, cantidad, datetime.now())
        )

    def ver_historico(self):
        for transaccion in self.transacciones:
            print(transaccion)

        print("=" * 25)

    def __add__(self, cantidad):
        if isinstance(cantidad, int) or isinstance(cantidad, float):
            msg = self.depositar(cantidad)
            return msg
        else:
            print("Debes sumar a la cuenta un entero o un flotante")

    def __sub__(self, cantidad):
        if isinstance(cantidad, int) or isinstance(cantidad, float):
            msg = self.retirar(cantidad)
            return msg
        else:
            print("Debes sumar a la cuenta un entero o un flotante")

    def depositar(self, cantidad):
        try:
            self.saldo += float(cantidad)
        except TypeError:
            raise InvalidoError("No puedes ingresar texto")
        """
        Podemos realizar una logica, en proyectos reales
        para verificar si la tarjeta usada para depositar
        tiene dinero o no
        """
        self.add_transaccion('Deposito', cantidad)

        return f'Ha depositado {cantidad}. El saldo actual de {self.nombre} es {self.saldo}'

    def se_puede_retirar(self, cantidad):
        return cantidad <= self.saldo

    def retirar(self, cantidad):
        try:
            cantidad = float(cantidad)
        except TypeError:
            raise InvalidoError("No puedes ingresar texto")
        if not self.se_puede_retirar(cantidad):
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        self.add_transaccion('Retirar', cantidad)
        return f'Su saldo actual es {self.saldo}'

    def consultar_saldo(self):
        return f'Su saldo actual es {self.saldo}'

    def transferir(self, cuenta_destino, cantidad):
        try:
            cantidad = float(cantidad)
        except TypeError:
            raise InvalidoError("No puedes ingresar texto")
        if not self.se_puede_retirar(cantidad):
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        cuenta_destino.depositar(cantidad)
        self.add_transaccion(f'Transferencia a {cuenta_destino}', cantidad)
        return f'Han sido transferidos {cantidad} a {cuenta_destino}', cuenta_destino