import math

num1 = float(input('A: '))

if num1 == 0:
    print('A equação não é do segundo grau')
else:
    num2 = float(input('B: '))
    num3 = float(input('C: '))
    delta = num2**2 - 4 * num1 * num3
    if delta < 0:
        print('Não possui raizes reais')
    elif delta == 0:
        raiz = (-num2)/(2 * num1)
        print(f'''Possui apenas uma raiz real.
A raiz é: {raiz}''')
    else:
        resultado1 = ((-num2) + math.sqrt(delta))/(2 * num1)
        resultado2 = ((-num2) - math.sqrt(delta))/(2 * num1)
        print(f'''Primeira raiz {resultado1}
Segunda raiz {resultado2}''')
