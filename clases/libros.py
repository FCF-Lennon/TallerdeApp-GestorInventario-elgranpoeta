from typing import MutableSequence
from clases.conectar import Conectar


class Libro:
    def __init__(self, codigo=0, nombre="", autor="", categoria=0, stock=0, editorial=0, bodega=0) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__autor = autor
        self.__categoria = categoria
        self.__stock = stock
        self.__bodega = bodega
        self.__editorial = editorial
        self.__conectar = Conectar()

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        self.__autor = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = value

    def insertarLibro(self):
        sql = f'INSERT INTO libro(nombre,autor,stock,categoriaID) VALUE("{self.__nombre}","{self.__autor}",{self.__stock},{self.__categoria})'
        mensaje = self.__conectar.ejecutar(sql)
        if mensaje == 1:
            mensaje = "Libro ingresado correctamente"
        return mensaje

    def listarLibros(self):
        sql = f"SELECT l.codigo, c.nombre,l.nombre,l.autor,l.stock FROM libro l JOIN categoria c WHERE l.categoriaID = c.categoriaID ORDER BY l.codigo DESC"
        listado = self.__conectar.listarTodo(sql)
        return listado

    def buscarLibro(self):
        sql = f"SELECT l.codigo,l.nombre,l.autor,l.stock,c.nombre FROM libro l JOIN categoria c WHERE l.codigo = {self.__codigo} AND l.categoriaID = c.categoriaID"
        listado = self.__conectar.listarTodo(sql)
        return listado

    def editarLibro(self):
        sql = f'UPDATE libro SET nombre = "{self.__nombre}", autor = "{self.__autor}", stock = {self.__stock}, categoriaID = {self.__categoria} WHERE codigo = {self.__codigo}'
        mensaje = self.__conectar.ejecutar(sql)
        if mensaje == 1:
            mensaje = 'Libro actualizado correctamente'
        return mensaje

    def eliminarLibro(self):
        sql = f"DELETE FROM libro WHERE codigo = {self.__codigo};"
        mensaje = self.__conectar.ejecutar(sql)
        if mensaje == 1:
            mensaje = "Libro eliminado correctamente"
        return mensaje
