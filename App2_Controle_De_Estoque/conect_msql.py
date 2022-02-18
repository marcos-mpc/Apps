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

    def executar(self, executar):
        self._cursor = self._cnx.cursor()
        self._cursor.execute(executar)
        self._cnx.commit()
        self._cnx.close()

    def mostrar(self):
        self._cursor = self._cnx.cursor()
        self._cursor.execute("SELECT * FROM produtos")
        rows = self._cursor.fetchall()
        for row in rows:
            for c in row:
                print(f'{c}', end=' ')
            print('\n')

