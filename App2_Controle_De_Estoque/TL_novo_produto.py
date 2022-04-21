from tkinter import *


def novo_produto():
    produto = Toplevel()
    produto.title('Novo Produto')
    produto.resizable(False, False)
    produto.geometry('743x130+300+300')

    larg = produto.winfo_screenwidth()
    alt = produto.winfo_screenheight()

    # dados da tela
    # labels
    lb = Label(produto)
    lb0 = Label(produto, text='CADASTRO DE PRODUTO',
                font=('verdana', 15, 'bold'),
                relief='ridge',
                width=52)
    lb1 = Label(produto, text='CODIGO',
                font=('verdana', 10, 'bold'),
                relief='groove',
                width=20)
    lb2 = Label(produto, text='PRODUTO',
                font=('verdana', 10, 'bold'),
                relief='groove',
                width=20)
    lb3 = Label(produto, text='TIPO UNITARIO',
                font=('verdana', 10, 'bold'),
                relief='groove',
                width=20)
    lb4 = Label(produto, text='QUANTIDADE',
                font=('verdana', 10, 'bold'),
                relief='groove',
                width=20)

    # entradas
    ent1 = Entry(produto, width=30)
    ent2 = Entry(produto, width=30)
    ent3 = Entry(produto, width=30)
    ent4 = Entry(produto, width=30)

    # botoes
    bt1 = Button(produto, text='Cadastrar')
    bt2 = Button(produto, text='Cancelar', command=lambda: produto.destroy())

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

    #botoes
    lb.grid(row=3, columnspan=4)
    bt1.grid(row=4, column=1, columnspan=2, sticky=E)
    bt2.grid(row=4, column=3, columnspan=2, sticky=W)
