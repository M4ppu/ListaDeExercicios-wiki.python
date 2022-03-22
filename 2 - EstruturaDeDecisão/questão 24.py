import math

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
operacao = input('Qual operação? (* + - /) ')

if operacao == '*':
    result = num1 * num2
elif operacao == '+':
    result = num1 + num2
elif operacao == '-':
    result = num1 - num2
elif operacao == '/':
    result = num1 / num2

resultR = math.floor(result)

par = resultR%2

if par == 0:
    x = 'par'
else:
    x = 'impar'

if result > 0:
    y = 'positivo'
else:
    y = 'negativo'

if result != resultR:
    z = 'decimal'
else:
    z = 'inteiro'

print(f'''O número é: {x}, {y} e {z}''')