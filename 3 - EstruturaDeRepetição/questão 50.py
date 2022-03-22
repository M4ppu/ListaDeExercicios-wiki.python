denLista = []
divLista = []

denominador = 1
divisor = 0

nVezes = int(input())

for i in range(0, nVezes):
    divisor = divisor + 1
    denLista.append(denominador)
    divLista.append(divisor)

print(f'H = ', end = '')

for i in range(len(denLista)):

    print(f'{denLista[i]}/{divLista[i]}', end = '')
    if i < (len(denLista)-1):
        print(' + ', end = '')
print(f' = {sum(denLista)}/{sum(divLista)}')