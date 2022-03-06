from tkinter import *

# configurações de tela
tela = Tk()
bg = PhotoImage(file='data/BG.png')
tela['bg'] = '#7FB098'
label_image = Label(tela, image=bg, bg='#7FB098')
label_image.place(x=350, y=85.33)
tela.state('zoomed')
tela.minsize(1320, 660)
tela.resizable(True, True)

# configurações de botões
image_entrada = PhotoImage(file='data/entrada.png').subsample(3)
image_saida = PhotoImage(file='data/saida.png').subsample(3)
image_cosulta = PhotoImage(file='data/pesquisar.png').subsample(3)
image_novo = PhotoImage(file='data/novo produto.png').subsample(3)

Button(tela, text='COSULTAR DADOS', font=('verdana', 16, 'italic'), image=image_cosulta, compound='top', bg='#9590B0').place(x=400, y=100)
Button(tela, text='NOVO PRODUTO', font=('verdana', 16, 'italic'), image=image_novo, compound='top', bg='#9590B0').place(x=400, y=420)
Button(tela, text='ABASTECER', font=('verdana', 16, 'italic'), image=image_entrada, compound='top', bg='#9590B0').place(x=800, y=100)
Button(tela, text='SAíDA', font=('verdana', 16, 'italic'), image=image_saida, compound='top', bg='#9590B0').place(x=800, y=420)


Label(tela, text='Marcos Pereira Chaves', bg='#7fb098', fg='#5E8270', font=('arial', 10, 'italic')).place(x=650, y=635)
tela.mainloop()

