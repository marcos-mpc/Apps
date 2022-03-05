from tkinter import *

# configurações de tela
tela = Tk()
bg = PhotoImage(file='data/BG.png')
tela['bg'] = '#7fb098'
label_image = Label(tela, image=bg, bg='#7fb098')
label_image.place(x=341.5, y=85.33)
tela.state('zoomed')
tela.minsize(1320, 660)
tela.resizable(True, True)

# configurações de botões
image_entrada = None
image_saida = None
image_cosulta = None
image_novo = PhotoImage(file='data/novo produto.png', height=80, width=80)

Button(tela, text='adicionar produto', image=image_novo, compound='top').pack()

tela.mainloop()

