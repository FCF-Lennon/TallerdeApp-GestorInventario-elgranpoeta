from clases.conectar import Conectar


class Categoria:
    def __init__(self):
        self.__conectar = Conectar()

    def listarCategorias(self):
        sql = "SELECT * FROM categoria"
        lista = self.__conectar.listarTodo(sql)
        return lista
