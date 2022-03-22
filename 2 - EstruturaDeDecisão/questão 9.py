num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

lista = [num1, num2, num3]

lista.sort()

print(lista[-1::-1])