valor = int(input('Valor do saque (10 até 600): '))

while valor < 10 or valor > 600:
    print('Valor inválido')
    valor = int(input('Valor do saque: '))

if valor >= 10 and valor <= 600:
    qtd100 = valor//100
    rest = valor%100
    qtd50 = rest//50
    rest = rest%50
    qtd10 = rest//10
    rest = rest%10
    qtd5 = rest//5
    rest = rest%5
    qtd1 = rest//1
    print(f'''Notas de 100: {qtd100}
Notas de 50: {qtd50}
Notas de 10: {qtd10}
Notas de 5: {qtd5}
Notas de 1: {qtd1}''')