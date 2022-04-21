from conexoes import Conector
from TL_estoque import *

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
def novo_produto():
    produto = Toplevel()
    produto.title('Novo Produto')
    produto.geometry('1350x670+1+9')


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
tabela.add_command(label='Cosultar Dados', command=Cosultar)
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

Button(tela, text='COSULTAR DADOS', command=Cosultar, font=('verdana', 16, 'italic'),
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
