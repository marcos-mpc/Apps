import tkinter
from tkinter import *
from connect_msql import Conector

obj = Conector()


class Cosultar:
    def __init__(self):
        self.dados = Toplevel()
        self.dados.title('Estoque')
        self.dados.geometry(f'1350x670+1+9')
        self.dados.resizable(False, False)
        self._inicio = 1
        self.bt1 = Button(self.dados, text='>', command=self.adicao)
        self.bt1.place(x=700, y=500, width=80)
        self.bt2 = Button(self.dados, text='<', command=self.subtracao, state=DISABLED)
        self.bt2.place(x=620, y=500, width=80)
        self._fim = 10

        # elementos da tela
        lb_id = Label(self.dados,
                      text='ID',
                      font=('verdana', 20, 'bold'),
                      relief='sunken',
                      width=4)
        lb_id.place(x=12, y=75)

        lb_codigo = Label(self.dados,
                          text='CÓDIGO',
                          font=('verdana', 20, 'bold'),
                          relief='sunken',
                          width=8)
        lb_codigo.place(x=97, y=75)

        lb_produto = Label(self.dados,
                           text='PRODUTO',
                           font=('verdana', 20, 'bold'),
                           relief='sunken',
                           width=9)
        lb_produto.place(x=258, y=75)

        lb_tipo_unitario = Label(self.dados,
                                 text='TIPO UNITÁRIO',
                                 font=('verdana', 20, 'bold'),
                                 relief='sunken',
                                 width=14)
        lb_tipo_unitario.place(x=438, y=75)

        lb_quantidade = Label(self.dados,
                              text='QUANTIDADE',
                              font=('verdana', 20, 'bold'),
                              relief='sunken',
                              width=12)
        lb_quantidade.place(x=713, y=75)

        lb_data = Label(self.dados,
                        text='ÚLTIMA ATUALIZAÇÃO',
                        font=('verdana', 20, 'bold'),
                        relief='sunken',
                        width=20)
        lb_data.place(x=950, y=75)

        lt = obj.mostrar()

        # ID
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in lt:
            lista.insert(END, c[0])
        lista.place(x=12, y=120, width=83, height=345)
        # CODIGO
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in lt:
            lista.insert(END, c[1])
        lista.place(x=97, y=120, width=159, height=345)
        # PRODUTOS
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in lt:
            lista.insert(END, c[2])
        lista.place(x=258, y=120, width=178, height=345)
        # TIPO UNITARIO
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in lt:
            lista.insert(END, c[3])
        lista.place(x=438, y=120, width=272, height=345)
        # QUANTIDADE
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in lt:
            lista.insert(END, c[4])
        lista.place(x=713, y=120, width=234, height=345)
        # DATA
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in lt:
            lista.insert(END, c[5])
        lista.place(x=950, y=120, width=385, height=345)

    def adicao(self):
        self._inicio += 10
        self._fim += 10
        if self._inicio > 1:
            self.bt2['state'] = NORMAL
        print(self._inicio)

    def subtracao(self):
        if self._inicio == 11:
            self._inicio = 1
            self._fim = 10
            self.bt2['state'] = DISABLED
            print(self._inicio)

        else:
            self._inicio -= 10
            self._fim -= 10

            print(self._inicio)
