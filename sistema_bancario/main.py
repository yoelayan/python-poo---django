from bank.cuenta import Cuenta
from bank.main import SistemaBanco

user = Cuenta(
    'Miguel',
    'miguelito@gmail.com',
    'abcdABCD1'
)

sistema = SistemaBanco()
sistema.agregar_usuario(user)
sistema.ejecutar()
