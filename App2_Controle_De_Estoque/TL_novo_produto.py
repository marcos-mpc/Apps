from tkinter import *


def novo_produto():
    produto = Toplevel()
    produto.title('Novo Produto')
    # dados da tela
    # labels
    lb0 = Label(produto, text='CADASTRO DE PRODUTO')
    lb1 = Label(produto, text='CODIGO')
    lb2 = Label(produto, text='PRODUTO')
    lb3 = Label(produto, text='TIPO UNITARIO')
    lb4 = Label(produto, text='QUANTIDADE')

    # entradas
    ent1 = Entry(produto)
    ent2 = Entry(produto)
    ent3 = Entry(produto)
    ent4 = Entry(produto)

    # layout da tela
    # labels
    lb0.grid(row=0, column=1, columnspan=4)
    lb1.grid(row=1, column=1)
    lb2.grid(row=1, column=2)
    lb3.grid(row=1, column=3)
    lb4.grid(row=1, column=4)

    # entradas
    ent1.grid(row=2, column=1)
    ent2.grid(row=2, column=2)
    ent3.grid(row=2, column=3)
    ent4.grid(row=2, column=4)
    # produto.geometry('1350x670+1+9')
