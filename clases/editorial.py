from clases.conectar import Conectar

class Editorial:
    def __init__(self):
        self.__conectar = Conectar()

    def listarEditorial(self):
        sql = "SELECT * FROM editorial"
        lista = self.__conectar.listarTodo(sql)
        return lista
