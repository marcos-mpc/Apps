from tkinter import *

# configurações de tela
tela = Tk()
w = tela.winfo_screenwidth()
h = tela.winfo_screenheight()
bg = PhotoImage(file='data/BG.png')
tela['bg'] = '#7fb098'
label_image = Label(tela, image=bg, bg='#7fb098')
label_image.place(x=w/4, y=h/9)
tela.state('zoomed')
tela.minsize(1320, 660)
tela.resizable(True, True)
tela.mainloop()
