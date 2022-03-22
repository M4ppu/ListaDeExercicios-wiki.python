dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

def data (dia, mes):
    if dia <= 31 and mes <= 12:
        return True
    else:
        print('Não é uma data válida')

print(str(dia) + '/' + str(mes) + '/' + str(ano))