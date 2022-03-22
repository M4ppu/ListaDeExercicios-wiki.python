numLista = []
multiplicacao = 1
soma = 0

for i in range(0, 5):
    num = int(input('Número ' + str(i + 1) + ': '))
    numLista.append(num)
for j in range(0, len(numLista)):
    multiplicacao = multiplicacao * numLista[j]
    soma = soma + numLista[j]

print(f'''
Números: {numLista}
Multiplicação: {multiplicacao}
Soma: {soma}''')