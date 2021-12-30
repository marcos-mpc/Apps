def imc():
    while True:
        try:
            p = float(input('Peso: '))
            a = float(str(input('Altura: ')).replace(',', '.'))
            if a > 100:
                a /= 100
            cal = str(f'{p / (a * a):.2f}')
        except ValueError:
            print('Erro! Digite um numero valido!')
        else:
            if float(cal) < 16:
                return f'IMC: {cal}, classe: Magreza Grau III'
            elif 16 < float(cal) < 16.99:
                return f'IMC: {cal}, classe: Magreza Grau II'
            elif 17 < float(cal) < 18.49:
                return f'IMC: {cal}, classe: Magreza Grau I'
            elif 18.5 < float(cal) < 24.99:
                return f'IMC: {cal}, classe: Adequado'
            elif 25 < float(cal) < 29.99:
                return f'IMC: {cal}, classe: Pré-Obeso'
            elif 30 < float(cal) < 34.99:
                return f'IMC: {cal}, classe: Obesidade Grau I'
            elif 35 < float(cal) < 39.99:
                return f'IMC: {cal}, classe: Obesidade Grau II'
            elif float(cal) >= 40:
                return f'IMC: {cal}, classe: Obesidade Grau III'


while True:
    print(f'{20*"="}\n{"CALCULO IMC":^20}\n{20*"="}')
    print(imc())
    while True:
        escl = input('Limpar [ 1 ]      Fechar [ 2 ]\n')
        if escl in '12':
            break
        print('Erro! Digite um numero valido!')
    if escl == '2':
        break
    else:
        continue

