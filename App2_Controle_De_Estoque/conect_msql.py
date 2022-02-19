import mysql.connector


class Conector:
    def __init__(self):
        self._user = 'root'
        self._password = ''
        self._host = 'localhost'
        self._database = 'estoque'
        self._cnx = mysql.connector.connect(user=self._user, password=self._password,
                                            host=self._host, database=self._database)
        self._cursor = None

    def executar(self, exe):
        self._cursor = self._cnx.cursor()
        self._cursor.execute(exe)
        self._cnx.commit()
        self._cnx.close()

    def mostrar(self, exe):
        self._cursor = self._cnx.cursor()
        self._cursor.execute(f"SELECT {exe} FROM produtos")
        rows = self._cursor.fetchall()
        for row in rows:
            for c in row:
                print(f'{c}', end=' ')
            print('\n')
