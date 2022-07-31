from clases.conectar import Conectar
class Usuario:
    def __init__(self, user="", password=""):
        self.__user = user
        self.__password = password
        self.__c = Conectar()

    def iniciarSesion(self):
        sql = f'SELECT correo, password, nombre FROM usuario WHERE correo = "{self.__user}" AND password = "{self.__password}" AND estado = 1'
        mensaje = self.__c.listarUno(sql)
        print(mensaje, 'linea 12 usuario')
        if mensaje:
            return mensaje

    def iniciarSesionAdmin(self):
        sql = f'SELECT correo,password, nombre FROM usuario WHERE correo = "{self.__user}" AND password = "{self.__password}" AND estado = 1 AND admin = 1'
        mensaje = self.__c.listarUno(sql)
        print(mensaje, 'linea 18 usuario')
        if mensaje:
            return mensaje
