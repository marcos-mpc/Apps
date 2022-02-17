import mysql.connector


class Conector:
    def __init__(self):
        self._user = 'root'
        self._password = ''
        self._host = 'localhost'
        self._database = 'estoque'

    def iniciar(self, executar):
        cnx = mysql.connector.connect(user=self._user, password=self._password,
                                      host=self._host, database=self._database)
        cursor = cnx.cursor()
        cursor.execute(executar)
        cnx.close()
