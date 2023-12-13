from dataclasses import dataclass


class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_actual, cantidad_retirada):
        super().__init__(f"Saldo insuficente: intentaste retirar {cantidad_retirada} pero solo tienes {saldo_actual}")
        self.saldo_actual = saldo_actual
        self.cantidad_retirada = cantidad_retirada


@dataclass
class InvalidoError(Exception):
    mensaje: str


class CuentaInvalidadError(InvalidoError):
    def __init__(self, mensaje='Cuenta no valida'):
        super().__init__(mensaje)


class OpcionInvalidaError(InvalidoError):
    def __init__(self):
        super().__init__(mensaje='Opcion no valida')
