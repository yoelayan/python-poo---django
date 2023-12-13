class clase_decoradora(object):
    def __init__(self, metodo):
        self.metodo = metodo

    def __call__(self, *args):
        print("Decorando la funcion")
        self.metodo(*args)


@clase_decoradora
def funcion_a_decorar(arg):
    print(arg)


funcion_a_decorar('Hola mundo')


class Generador:
    def __init__(self, lista_claves, maximo):
        self.lista_claves = lista_claves
        self.maximo = maximo

    def __iter__(self):
        self.numero = 0
        return self

    def __next__(self):
        if self.numero <= self.maximo:
            resultado = 2 ** self.numero
            self.numero += 1
            return resultado, self.lista_claves, 'mensagito'
        else:
            raise StopIteration


for resultado, lista_claves, mensagito in Generador(['abc', '123', 'a1b2c3'], 5):
    print(resultado, lista_claves, mensagito)
