from clases.conectar import Conectar


class Usuario:
    c = Conectar()

    def __init__(self, user="", password=""):
        self.__user = user
        self.__password = password

    def iniciarSesion(self):
        sql = f'SELECT correo,password,nombre FROM usuario WHERE correo = "{self.__user}" AND password = "{self.__password}" AND estado = 1'
        mensaje = self.c.listarUno(sql)
        if mensaje:
            return mensaje

    def iniciarSesionAdmin(self):
        sql = f'SELECT correo,password,nombre FROM usuario WHERE correo = "{self.__user}" AND password = "{self.__password}" AND estado = 1 AND admin = 1'
        mensaje = self.c.listarUno(sql)
        if mensaje:
            return mensaje
