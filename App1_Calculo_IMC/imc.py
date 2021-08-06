from tkinter import *


# Função Principal
def imc():
    p = float(entrada_peso.get())
    a = float(entrada_altura.get())
    if a > 100:
        a /= 100
    cal = str(f'{p / (a*a):.2f}')
    if float(cal) < 16:
        result_classe.set('Magreza Grau III')
    elif 16 < float(cal) < 16.9:
        result_classe.set('Magreza Grau II')
    elif 17 < float(cal) < 18.4:
        result_classe.set('Magreza Grau II')
    elif 18.5 < float(cal) < 24.9:
        result_classe.set('Adequado')
    elif 25 < float(cal) < 29.9:
        result_classe.set('Pré-Obeso')
    elif 30 < float(cal) < 34.9:
        result_classe.set('Obesidade Grau I')
    elif 35 < float(cal) < 39.9:
        result_classe.set('Obesidade Grau II')
    elif float(cal) >= 40:
        result_classe.set('Obesidade Grau III')
    result_imc.set(cal)


lista = ['Abaixo de 16 : Magreza Grau III ', '16 a 16,9 : Magreza Grau II', '17 a 18,4 : Magreza Grau II ',
                '18,5 a 24,9 : Adequado ', '25 a 29,9 : Pré-Obeso', '30 a 34,9 : Obesidade Grau I',
                '35 a 39,9 : Obesidade Grau II', 'Acima de 40 : Obesidade Grau III']
# Tela
tela = Tk()
tela.title('Calculo De IMC')
tela.iconbitmap('data/icone.ico')
result_imc = StringVar()
result_classe = StringVar()
tela.resizable(False, False)
tela['bg'] = '#c7fdff'


# Elementos
Titulo_Programa = Label(tela, text='Calculo De IMC', font='verdana 16 bold', width=18, bg='#e3733b', bd=2, relief='raised')

txt_peso = Label(tela, text='Peso', font='verdana 12 bold', width=12, bg='#c7fdff')
txt_altura = Label(tela, text='Altura', font='verdana 12 bold', width=12,  bg='#c7fdff')
txt_imc = Label(tela,textvariable= result_imc, bg='#c7fdff')
txt_clase = Label(tela, textvariable= result_classe, bg='#c7fdff')
txt_imc_result = Label(tela, text='IMC', bg='#c7fdff')
txt_clase_result = Label(tela, text='Classe', bg='#c7fdff')

entrada_peso = Entry(tela)
entrada_altura = Entry(tela)

bto = Button(tela, text='Calcular', command=imc, bg='#e3733b')

lista1 = Listbox(tela, width=30,bg='#c7fdff')
for c in lista:
    lista1.insert(0, c)


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

bto.grid(columnspan=2, sticky=S)

lista1.grid(columnspan=2, sticky=S)

tela.mainloop()