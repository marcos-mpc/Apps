from tkinter import *
from connect_msql import Conector

obj = Conector()

# configurações de telas
# Tela Principal
tela = Tk()
tela.title('Controle De Estoque')
bg = PhotoImage(file='data/BG.png')
tela['bg'] = '#7FB098'
label_image = Label(tela, image=bg, bg='#7FB098')
label_image.place(x=350, y=85.33)
tela.state('zoomed')
tela.minsize(1320, 660)
tela.resizable(True, True)


# Tela de dados
def cosultar_dados():
    dados = Toplevel()
    dados.title('Estoque')
    dados.geometry(f'1350x670+1+9')
    dados.resizable(False, False)

# elementos da tela
    lb_id = Label(dados, text='ID', font=('verdana', 20, 'bold'), relief='sunken', width=4)
    lb_id.place(x=12, y=75)

    lb_codigo = Label(dados, text='CÓDIGO', font=('verdana', 20, 'bold'), relief='sunken', width=8)
    lb_codigo.place(x=97, y=75)

    lb_produto = Label(dados, text='PRODUTO', font=('verdana', 20, 'bold'), relief='sunken', width=9)
    lb_produto.place(x=258, y=75)

    lb_tipo_unitario = Label(dados, text='TIPO UNITÁRIO', font=('verdana', 20, 'bold'), relief='sunken', width=14)
    lb_tipo_unitario.place(x=438, y=75)

    lb_quantidade = Label(dados, text='QUANTIDADE', font=('verdana', 20, 'bold'), relief='sunken', width=12)
    lb_quantidade.place(x=713, y=75)

    lb_data = Label(dados, text='ÚLTIMA ATUALIZAÇÃO', font=('verdana', 20, 'bold'), relief='sunken', width=20)
    lb_data.place(x=950, y=75)

    lt = obj.mostrar()
    # ID
    lista = Listbox(dados, relief='sunken', font=('verdana', 20), justify=CENTER)
    for c in lt:
        lista.insert(END, c[0])
    lista.place(x=12, y=120, width=83, height=345)
    # CODIGO
    lista = Listbox(dados, relief='sunken', font=('verdana', 20), justify=CENTER)
    for c in lt:
        lista.insert(END, c[1])
    lista.place(x=97, y=120, width=159, height=345)
    # PRODUTOS
    lista = Listbox(dados, relief='sunken', font=('verdana', 20), justify=CENTER)
    for c in lt:
        lista.insert(END, c[2])
    lista.place(x=258, y=120, width=178, height=345)
    # TIPO UNITARIO
    lista = Listbox(dados, relief='sunken', font=('verdana', 20), justify=CENTER)
    for c in lt:
        lista.insert(END, c[3])
    lista.place(x=438, y=120, width=272, height=345)
    # QUANTIDADE
    lista = Listbox(dados, relief='sunken', font=('verdana', 20), justify=CENTER)
    for c in lt:
        lista.insert(END, c[4])
    lista.place(x=713, y=120, width=234, height=345)
    # DATA
    lista = Listbox(dados, relief='sunken', font=('verdana', 20), justify=CENTER)
    for c in lt:
        lista.insert(END, c[5])
    lista.place(x=950, y=120, width=385, height=345)


def novo_produto():
    novo = Toplevel()
    novo.title('Novo Produto')
    novo.geometry('1350x670+1+9')


def abastecer():
    entrada = Toplevel()
    entrada.title('Abastecer')
    entrada.geometry('1350x670+1+9')


def saida():
    sd = Toplevel()
    sd.title('Saida')
    sd.geometry('1350x670+1+9')


# configuração de menu
menu = Menu(tela)
tabela = Menu(menu, tearoff=0)
tabela.add_command(label='Novo Produto', command=novo_produto)
tabela.add_command(label='Cosultar Dados', command=cosultar_dados)
menu.add_cascade(label='Tabela', menu=tabela)

estoque = Menu(menu, tearoff=0)
estoque.add_command(label='Abastecer', command=abastecer)
estoque.add_command(label='Saida', command=saida)
menu.add_cascade(label='Estoque', menu=estoque)

tela.config(menu=menu)

# configurações de botões
image_entrada = PhotoImage(file='data/entrada.png').subsample(3)
image_saida = PhotoImage(file='data/saida.png').subsample(3)
image_cosulta = PhotoImage(file='data/pesquisar.png').subsample(3)
image_novo = PhotoImage(file='data/novo produto.png').subsample(3)

Button(tela, text='COSULTAR DADOS', command=cosultar_dados, font=('verdana', 16, 'italic'),
       image=image_cosulta, compound='top',
       bg='#9590B0').place(x=400, y=100)

Button(tela, text='NOVO PRODUTO', command=novo_produto,  font=('verdana', 16, 'italic'),
       image=image_novo, compound='top', bg='#9590B0')\
    .place(x=400, y=420)

Button(tela, text='ABASTECER', command=abastecer, font=('verdana', 16, 'italic'),
       image=image_entrada, compound='top', bg='#9590B0')\
    .place(x=800, y=100)

Button(tela, text='SAíDA', command=saida, font=('verdana', 16, 'italic'),
       image=image_saida, compound='top', bg='#9590B0')\
    .place(x=800, y=420)

Label(tela, text='Marcos Pereira Chaves', bg='#7fb098', fg='#5E8270',
      font=('arial', 10, 'italic')).place(x=650, y=635)

tela.mainloop()
