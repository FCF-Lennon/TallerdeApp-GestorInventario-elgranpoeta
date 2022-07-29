from clases.conectar import Conectar

class Bodega:
    def __init__(self):
        self.__conectar = Conectar()

    def listarBodega(self):
        sql = "SELECT * FROM bodega"
        lista = self.__conectar.listarTodo(sql)
        return lista
