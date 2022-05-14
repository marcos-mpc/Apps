from tkinter import *
from tkinter import messagebox
from conex_funxoes import adicionar


class Cadastro:
    def __init__(self):
        self.codigo = StringVar()
        self.produtos = StringVar()
        self.tipunit = StringVar()
        self.quantidade = StringVar()

        self.produto = Toplevel()
        self.produto.title('Novo Produto')
        self.produto.resizable(False, False)
        self.produto.geometry('743x130+300+300')

        # dados da tela
        # labels
        lb = Label(self.produto)
        lb0 = Label(self.produto, text='CADASTRO DE PRODUTO',
                    font=('verdana', 15, 'bold'),
                    relief='ridge',
                    width=52)
        lb1 = Label(self.produto, text='CODIGO',
                    font=('verdana', 10, 'bold'),
                    relief='groove',
                    width=20)
        lb2 = Label(self.produto, text='PRODUTO',
                    font=('verdana', 10, 'bold'),
                    relief='groove',
                    width=20)
        lb3 = Label(self.produto, text='TIPO UNITARIO',
                    font=('verdana', 10, 'bold'),
                    relief='groove',
                    width=20)
        lb4 = Label(self.produto, text='QUANTIDADE',
                    font=('verdana', 10, 'bold'),
                    relief='groove',
                    width=20)

        # entradas
        ent1 = Entry(self.produto, width=30, textvariable=self.codigo)
        ent2 = Entry(self.produto, width=30, textvariable=self.produtos)
        ent3 = Entry(self.produto, width=30, textvariable=self.tipunit)
        ent4 = Entry(self.produto, width=30, textvariable=self.quantidade)

        # botoes
        bt1 = Button(self.produto, text='Cadastrar', command=self.informacoes)

        bt2 = Button(self.produto,
                     text='Cancelar',
                     command=lambda: self.produto.destroy())

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

        # botoes
        lb.grid(row=3, columnspan=4)
        bt1.grid(row=4, column=1, columnspan=2, sticky=E)
        bt2.grid(row=4, column=3, columnspan=2, sticky=W)

    def informacoes(self):
        try:
            var_codigo = int(self.codigo.get())
            var_produto = str(self.produtos.get()).upper()
            var_tipunit = str(self.tipunit.get()).upper()
            var_quantidade = int(self.quantidade.get())
            adicionar(var_codigo, var_produto, var_tipunit, var_quantidade)
            messagebox.showinfo('Cadastro Concluído', 'Produto cadastrado com sucesso')

        except ValueError:
            messagebox.showerror('Erro!', 'Informações invalidas. Tente novamente!')
