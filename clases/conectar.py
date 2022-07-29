import mysql.connector


class Conectar:
    def __init__(self) -> None:
        self.__db = mysql.connector.connect(
            host="localhost", user="root", password="", database="elgranpoeta"
        )

        self.__cursor = self.__db.cursor()

    def ejecutar(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__db.commit()

            rowcount = self.__cursor.rowcount

            return rowcount

        except mysql.connector.Error as e:
            return "Error: " + str(e)

    def listarTodo(self, sql):
        try:
            self.__cursor.execute(sql)
            listado = self.__cursor.fetchall()
            return listado

        except mysql.connector.Error as e:
            return "Error: " + str(e)

    def listarUno(self, sql):
        try:
            self.__cursor.execute(sql)
            listado = self.__cursor.fetchone()
            return listado

        except mysql.connector.Error as e:
            return "Error: " + str(e)
