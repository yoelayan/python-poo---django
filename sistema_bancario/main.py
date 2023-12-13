from bank.cuenta import Cuenta
from auth.user import Usuario
from bank.main import SistemaBanco

cuenta = Cuenta(
    'Miguel',
    'miguelito@gmail.com',
    'abcdABCD1'
)

# Sumamos por defecto 1000 al saldo de la cuenta
msg = cuenta + 1000
print(msg)

msg = cuenta - 200
print(msg)

sistema = SistemaBanco()

Usuario.agregar_usuario(sistema.usuarios, cuenta)
sistema.ejecutar()
