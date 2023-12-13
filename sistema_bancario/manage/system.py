from auth.user import Usuario


class System:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def login_usuario(self, email, password):
        usuario = self.buscar_usuario(email)
        if usuario:
            return usuario.autenticar(password)
        return False
