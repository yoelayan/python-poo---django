from manage.system import System
from bank.exceptions import (
    CuentaInvalidadError, SaldoInsuficienteError
)
from .cuenta import Cuenta
from auth.user import Usuario


class SistemaBanco(System):
    def __init__(self):
        super().__init__()

    @property
    def opciones_disponibles(self):
        return {
            '1': ('depositar', 'Ingrese la cantidad a depositar: '),
            '2': ('retirar', 'Ingrese la cantidad a retirar: '),
            '3': ('consultar_saldo', ''),
            '4': ('transferir', [
                'Ingrese el email de la cuenta destino',
                'Ingrese la cantidad a transferir: '
                ]),
            '5': ('ver_historico', ''),
            '6': ('logout', '')
        }

    def mostrar_opciones(self):
        print("\n1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Transferir dinero a otra cuenta")
        print("5. Consultar Transacciones")
        print("6. Salir")

    def ejecutar(self):
        while True:
            try:
                print("\n Seleccione un email: ")
                for usuario in self.usuarios:
                    print(usuario)
            except (CuentaInvalidadError, SaldoInsuficienteError) as e:
                print(e)

            email_seleccionado = input()
            usuario_seleccionado: Cuenta = Usuario.buscar_usuario(
                self.usuarios,
                email_seleccionado
            )
            if not usuario_seleccionado:
                raise CuentaInvalidadError()

            password = input("Ingrese su password: ")
            if not usuario_seleccionado.autenticar(password):
                raise CuentaInvalidadError("Password incorrecto")

            while usuario_seleccionado.esta_logueado:
                print("Usuario logueado: ", usuario_seleccionado)
                self.mostrar_opciones()
                opcion = input("Seleccione una opcion: ")

                metodo, mensajes = self.opciones_disponibles[opcion]

                entradas = []

                if isinstance(mensajes, str):
                    print(mensajes)
                    if mensajes:
                        entradas.append(input())
                elif isinstance(mensajes, list):
                    for mensaje in mensajes:
                        print(mensaje)
                        entradas.append(input())
                msg = getattr(usuario_seleccionado, metodo)(*entradas)
                print(msg)
            print("Gracias por usar nuestro banco, hasta pronto!")
