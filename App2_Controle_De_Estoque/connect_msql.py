import mysql.connector


class Conector:
    """conecta o mysql ao python"""

    def __init__(self):
        self._user = 'root'
        self._password = ''
        self._host = 'localhost'
        self._database = 'estoque'
        self._cnx = mysql.connector.connect(user=self._user, password=self._password,
                                            host=self._host, database=self._database)
        self._cursor = None

    def executar(self, exe):
        """executa comandos de manipulação de dados"""
        self._cursor = self._cnx.cursor()
        self._cursor.execute(exe)
        self._cnx.commit()
        self._cnx.close()

    def mostrar(self, exe='*', inicio='1', fim='10'):
        """executa comados de visualização de dados"""
        self._cursor = self._cnx.cursor()
        self._cursor.execute(f"SELECT {exe} FROM produtos "
                             f"WHERE id BETWEEN {inicio} AND {fim}")
        lt = []
        rows = self._cursor.fetchall()
        return rows


if __name__ == '__main__':
    obj = Conector()
    print(obj.mostrar())
