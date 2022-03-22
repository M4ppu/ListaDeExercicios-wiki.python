nota = float(input('Uma nota de 0 até 10: '))

while nota < 0 or nota > 10:
    print('Nota inválida')
    nota = float(input('Uma nota de 0 até 10: '))
if nota >= 0 and nota <= 10:
    print('A nota é: ' + str(nota))