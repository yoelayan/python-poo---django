from dataclasses import dataclass
import math


@dataclass
class Fraccion:
    numerador: int
    denominador: int

    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    def simplificar(self):
        gran_comun_divisor = math.gcd(self.numerador, self.denominador)
        print(f"Simplificado de {self} es: ", gran_comun_divisor)
        return Fraccion(
            self.numerador//gran_comun_divisor,
            self.denominador//gran_comun_divisor
        )

    def __add__(self, otra_fraccion):
        if not isinstance(otra_fraccion, Fraccion):
            raise TypeError("Solo se puede sumar una fraccion con otra")
        numerador = self.numerador * otra_fraccion.denominador +\
            self.denominador * otra_fraccion.denominador
        denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(numerador, denominador).simplificar()

    def __sub__(self, otra_fraccion):
        numerador = self.numerador * otra_fraccion.denominador -\
            self.denominador * otra_fraccion.numerador
        denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(numerador, denominador).simplificar()

    def __mul__(self, otra_fraccion):
        numerador = self.numerador * otra_fraccion.numerador
        denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(numerador, denominador).simplificar()

    def __truediv__(self, otra_fraccion):
        numerador = self.numerador * otra_fraccion.denominador
        denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(numerador, denominador).simplificar()

    def __eq__(self, otra_fraccion):
        return self.numerador * otra_fraccion.denominador ==\
            self.denominador * otra_fraccion.numerador

    def __ne__(self, otra_fraccion):
        return not self.__eq__(otra_fraccion)

    def __lt__(self, otra_fraccion):
        return self.numerador * otra_fraccion.denominador <\
            self.denominador * otra_fraccion.numerador

    def __le__(self, otra_fraccion):
        return self.__lt__(otra_fraccion) or self.__eq__(otra_fraccion)

    def __gt__(self, otra_fraccion):
        return not self.__le__(otra_fraccion)

    def __ge__(self, otra_fraccion):
        return not self.__lt__(otra_fraccion)


f1 = Fraccion(1, 2).simplificar()
f2 = Fraccion(2, 4).simplificar()

print(f1 + f2)


@dataclass
class Vector:
    x: int
    y: int

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, otro_vector):
        if not isinstance(otro_vector, Vector):
            raise TypeError("Solo se pueden sumar un vector con otro")
        return Vector(self.x + otro_vector.x, self.y + otro_vector.y)

    def producto_punto(self, otro_vector):
        return self.x * otro_vector.x + self.y * otro_vector.y


v1 = Vector(1, 2)
v2 = Vector(2, 4)

print((v1 + v2).producto_punto(v2))
