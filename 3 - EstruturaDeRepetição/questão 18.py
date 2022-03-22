quant = int(input('Quantidade de nº: '))
maior = 0
menor = 0
soma = 0

for i in range(0, quant):
    num1 = float(input())
    if num1 > maior:
        maior = num1
    if i == 0:
        maior = num1
        menor = num1
    if num1 < menor:
        menor = num1
    soma = soma + num1

print(f'''Maior nº: {maior}
Menor nº: {menor}
Soma de todos: {soma}''')