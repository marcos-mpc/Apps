from mysql.connector import Error
from conexoes import *
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


def renomear(tupla, alteracao, iden):
    """renomeia alguma coisa da tabela"""
    try:
        obj.executar(f"UPDATE produtos SET {tupla}= '{alteracao}' WHERE id ='{iden}'")
    except Error:
        print('ERRO! Refaça o processo!')


def entrada_de_produto(valor, iden):
    try:
        obj.executar(f"UPDATE produtos SET quantidade= (quantidade + '{valor}') WHERE id ='{iden}'")
    except Error:
        print('ERRO! Refaça o processo!')


def saida_de_produto(valor, iden):
    try:
        obj.executar(f"UPDATE produtos SET quantidade= (quantidade - '{valor}') WHERE id ='{iden}'")
    except Error:
        print('ERRO! Refaça o processo!')
