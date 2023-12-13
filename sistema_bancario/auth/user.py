import base64
import re
from .exceptions import PasswordWek


class Usuario:
    def __init__(self, nombre, email, password):
        if self.validar_fuerza_password(password):
            self.nombre = nombre
            self.email = email
            self.password = self.encriptar_password(password)
            self.esta_logueado = False

    def __str__(self):
        return f'{self.nombre} : {self.email}'

    class Meta:
        abstract = True

    def actualizar(
            self, nombre: str = None, email: str = None, password: str = None):
        if nombre:
            self.nombre = nombre
        elif email:
            self.email = email
        elif password:
            self.password = self.encriptar_password(password)
        else:
            print("No se ha actualizado ningun atributo")

    def encriptar_password(self, password):
        return base64.b64encode(password.encode())

    def desencriptar_password(self, passowrd_encode):
        return base64.b64decode(passowrd_encode).decode()

    def validar_fuerza_password(self, password):
        es_cuatro_mayusculas = len(re.findall('[A-Z]', password)) >= 4
        es_cuatro_minusculas = len(re.findall('[a-z]', password)) >= 4
        contiene_numero = re.search(r'\d', password)

        if es_cuatro_mayusculas and es_cuatro_minusculas \
                and contiene_numero:
            return True

        mensaje = ''
        if not es_cuatro_mayusculas:
            mensaje += 'Faltan cuatro mayusculas \n'
        if not es_cuatro_minusculas:
            mensaje += 'Faltan cuatro minusculas \n'
        if not contiene_numero:
            mensaje += 'Falta por lo menos un digito'
        raise PasswordWek(mensaje)

    def check_password(self, password):
        print(self.desencriptar_password(self.password) == password)
        return self.desencriptar_password(self.password) == password

    def autenticar(self, password):
        if self.check_password(password):
            self.esta_logueado = True
            return True
        return False

    def logout(self):
        self.esta_logueado = False
