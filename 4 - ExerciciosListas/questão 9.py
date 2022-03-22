numLista = []
soma = 0

for i in range(0, 10):
    num = int(input(f'Número inteiro {i + 1}: '))
    numLista.append(num)
for j in range(0, len(numLista)):
    soma = soma + (numLista[j]**2)

print(f'Soma dos quadrados: {soma}')