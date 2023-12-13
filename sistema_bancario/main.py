from bank.cuenta import Cuenta
from auth.user import Usuario
from bank.main import SistemaBanco
import json


with open('jsons/users.json') as file:
    usuarios_json = json.load(file)


sistema = SistemaBanco()
for usuario in usuarios_json:
    cuenta = Cuenta(
        nombre=usuario['nombre'],
        email=usuario['email'],
        password=usuario['password']
    )
    cuenta + 100000
    Usuario.agregar_usuario(sistema.usuarios, cuenta)

sistema.ejecutar()
