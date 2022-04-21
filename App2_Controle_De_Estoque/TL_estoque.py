from tkinter import *
from conexoes import Conector

obj = Conector()
quantidade = obj.mostrar_soma()


class Cosultar:
    def __init__(self):
        self.dados = Toplevel()
        self.dados.title('Estoque')
        self.dados.geometry(f'1350x670+1+9')
        self.dados.resizable(False, False)
        self._inicio = 1
        self._fim = 10
        self.bt1 = Button(self.dados, text='>', command=self.adicao)
        self.bt2 = Button(self.dados, text='<', command=self.subtracao, state=DISABLED)
        if quantidade > 10:
            self.bt1.place(x=700, y=500, width=80)
            self.bt2.place(x=620, y=500, width=80)
        self.lt = obj.mostrar(inicio=self._inicio, fim=self._fim)
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
        self.mostrar(self._inicio, self._fim)

    def mostrar(self, inicio, fim):
        self.lt = obj.mostrar(inicio=inicio, fim=fim)
        # ID
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)

        for c in self.lt:
            lista.insert(END, c[0])
        lista.place(x=12, y=120, width=83, height=345)
        # CODIGO
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in self.lt:
            lista.insert(END, c[1])
        lista.place(x=97, y=120, width=159, height=345)
        # PRODUTOS
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in self.lt:
            lista.insert(END, c[2])
        lista.place(x=258, y=120, width=178, height=345)
        # TIPO UNITARIO
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in self.lt:
            lista.insert(END, c[3])
        lista.place(x=438, y=120, width=272, height=345)
        # QUANTIDADE
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in self.lt:
            lista.insert(END, c[4])
        lista.place(x=713, y=120, width=234, height=345)
        # DATA
        lista = Listbox(self.dados,
                        relief='sunken',
                        font=('verdana', 20),
                        justify=CENTER)
        for c in self.lt:
            lista.insert(END, c[5])
        lista.place(x=950, y=120, width=385, height=345)

    def adicao(self):
        lt = []
        lt.clear()
        self._inicio += 10
        self._fim += 10
        for c in range(self._inicio, self._fim+1):
            lt.append(c)
        if quantidade in lt:
            self.bt1['state'] = DISABLED
        if self._inicio > 1:
            self.bt2['state'] = NORMAL
        self.mostrar(self._inicio, self._fim)

    def subtracao(self):
        if self._inicio == 11:
            self._inicio = 1
            self._fim = 10
            self.bt2['state'] = DISABLED
            self.mostrar(self._inicio, self._fim)
            self.bt1['state'] = NORMAL
        else:
            self._inicio -= 10
            self._fim -= 10
            self.mostrar(self._inicio, self._fim)
            self.bt1['state'] = NORMAL
