import mysql.connector

cnx = mysql.connector.connect(user='root', password='', host='localhost', database='estoque')
cursor = cnx.cursor()

cnx.close()
