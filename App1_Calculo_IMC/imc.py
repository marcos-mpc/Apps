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


dicionario = {'Magreza Grau III': 'abaixo de 16', 'Magreza Grau II': '16 a 16,9', 'Magreza Grau II': '17 a 18,4',
                'Adequado': '18,5 a 24,9', 'Pré-Obeso': '25 a 29,9', 'Obesidade Grau I': '30 a 34,9',
                'Obesidade Grau II': '35 a 39,9', 'Obesidade Grau III': 'acima de 40'}
# Tela
tela = Tk()
result_imc = StringVar()
result_classe = StringVar()
# Elementos
Titulo_Programa = Label(tela, text='Calculo De IMC', font='verdana 16 bold')
txt_peso = Label(tela, text='Peso', font='verdana 12 bold')
txt_altura = Label(tela, text='Altura', font='verdana 12 bold')
txt_imc = Label(tela, textvariable= result_imc)
txt_clase = Label(tela, textvariable= result_classe)
entrada_peso = Entry(tela)
entrada_altura = Entry(tela)
bto = Button(tela, text='Calcular', command=imc)
lista1 = Listbox(tela, justify=CENTER)
lista2 = Listbox(tela, justify=CENTER)

for i, v in dicionario.items():
    lista1.insert(0, i)
    lista2.insert(0, v)

# layout
Titulo_Programa.grid(columnspan=2, sticky=N)
txt_peso.grid(row=1, column=0, sticky=W)
txt_altura.grid(row=2, column=0, sticky=W)
txt_imc.grid(row=3, column=0)
txt_clase.grid(row=3, column=1)
entrada_peso.grid(row=1, column=1)
entrada_altura.grid(row=2, column=1)
bto.grid(columnspan=2, sticky=S)
lista1.grid(row=4, column=0)
lista2.grid(row=4, column=1)
tela.mainloop()