class Transaccion:

    def __init__(self, tipo, cantidad, fecha):
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha

    def __str__(self) -> str:
        return f'{self.tipo} - {self.cantidad} : {self.fecha}'
