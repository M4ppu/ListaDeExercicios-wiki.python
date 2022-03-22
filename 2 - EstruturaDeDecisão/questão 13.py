diaDaSemana = int(input('Dia da semana: '))

lista = [1, 2, 3, 4, 5, 6, 7]

while diaDaSemana not in lista:
    print('Valor inválido')
    diaDaSemana = int(input('Diz um válido: '))
if diaDaSemana == 1:
    print('Domingo')
elif diaDaSemana == 2:
    print('Segunda')
elif diaDaSemana == 3:
    print('Terça')
elif diaDaSemana == 4:
    print('Quarta')
elif diaDaSemana == 5:
    print('Quinta')
elif diaDaSemana == 6:
    print('Sexta')
elif diaDaSemana == 7:
    print('Sábado')