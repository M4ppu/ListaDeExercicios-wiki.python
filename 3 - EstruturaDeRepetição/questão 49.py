from fractions import Fraction
import fractions

denLista = []
divLista = []

denominador = 0
divisor = 0

nVezes = int(input())

soma = 0

for i in range(0, nVezes):
    if i == 0:
        denominador = denominador + 1
        divisor = divisor + 1
        denLista.append(denominador)
        divLista.append(divisor)
    else:
        denominador = denominador + 1
        divisor = divisor + 2
        denLista.append(denominador)
        divLista.append(divisor)

print(f'S = ', end = '')

for i in range(len(denLista)):

    print(f'{denLista[i]}/{divLista[i]}', end = '')
    if i < (len(denLista)-1):
        print(' + ', end = '')
    soma = soma + (denLista[i] / divLista[i])
print(f' = {str(Fraction(soma).limit_denominator())}')