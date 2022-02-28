from mysql.connector import Error
from connect_msql import Conector
from datetime import date


obj = Conector()


def adicionar(cod, produto, tipo_unitario, quantidade):
    """inserir novo produto a tabela"""
    try:
        obj.executar(f"INSERT INTO produtos VALUES(default, '{cod}', '{produto}',"
                     f"'{tipo_unitario}', '{quantidade}', '{date.today()}')")
    except Error:
        print('ERRO! Refaça o processo!')


def excluir(identificador):
    """deletar produto da tabela utilizando o id"""
    obj.executar(f"DELETE FROM produtos WHERE id = '{identificador}'")


def renomear():
    pass


def entrada_de_produto():
    pass


def saida_de_produto():
    pass


excluir('12')
