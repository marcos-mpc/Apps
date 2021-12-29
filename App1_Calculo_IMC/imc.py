from tkinter import *
from time import sleep


def imc():
    p = float(entrada_peso.get())
    a = float(entrada_altura.get())
    if a > 100:
        a /= 100
    cal = str(f'{p / (a * a):.2f}')
    if float(cal) < 16:
        result_classe.set('Magreza Grau III')
    elif 16 < float(cal) < 16.99:
        result_classe.set('Magreza Grau II')
    elif 17 < float(cal) < 18.49:
        result_classe.set('Magreza Grau I')
    elif 18.5 < float(cal) < 24.99:
        result_classe.set('Adequado')
    elif 25 < float(cal) < 29.99:
        result_classe.set('Pré-Obeso')
    elif 30 < float(cal) < 34.99:
        result_classe.set('Obesidade Grau I')
    elif 35 < float(cal) < 39.99:
        result_classe.set('Obesidade Grau II')
    elif float(cal) >= 40:
        result_classe.set('Obesidade Grau III')
    sleep(0.5)
    result_imc.set(cal)


def lp():
    result_classe.set('')
    result_imc.set('')
    entrada_peso.delete(0, 'end')
    entrada_altura.delete(0, 'end')
    entrada_peso.focus()


# Tela
tela = Tk()
tela.title('Calculo De IMC')
tela.iconbitmap('data/icone.ico')
result_imc = StringVar()
result_classe = StringVar()
tela.resizable(False, False)
tela['bg'] = '#c7fdff'

# Elementos
Titulo_Programa = Label(tela, text='Calculo De IMC', font='verdana 16 bold', width=18, bg='#e3733b', bd=2,
                        relief='raised')

txt_peso = Label(tela, text='Peso', font='verdana 12 bold', width=12, bg='#c7fdff')
txt_altura = Label(tela, text='Altura', font='verdana 12 bold', width=12, bg='#c7fdff')
txt_imc = Label(tela, textvariable=result_imc, bg='#c7fdff')
txt_clase = Label(tela, textvariable=result_classe, bg='#c7fdff')
txt_imc_result = Label(tela, text='IMC', bg='#c7fdff')
txt_clase_result = Label(tela, text='Classe', bg='#c7fdff')

entrada_peso = Entry(tela)
entrada_altura = Entry(tela)

bto = Button(tela, text='Calcular', command=imc, bg='#e3733b', width=15)
bto2 = Button(tela, text='Limpar', bg='#e3733b', command=lp, width=15)


# layout
Titulo_Programa.grid(columnspan=2, sticky=N)

txt_peso.grid(row=1, column=0, sticky=W)
txt_altura.grid(row=2, column=0, sticky=W)
txt_imc_result.grid(row=3, column=0)
txt_imc.grid(row=4, column=0)
txt_clase_result.grid(row=3, column=1)
txt_clase.grid(row=4, column=1)

entrada_peso.grid(row=1, column=1)
entrada_altura.grid(row=2, column=1)

bto.grid(row=5, column=0)
bto2.grid(row=5, column=1)

tela.mainloop()
