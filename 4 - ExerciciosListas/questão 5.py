numeros = []
par = []
impar = []

for i in range(0, 20):
    num = int(input('Número ' + str(i + 1) + ': '))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'''
Números: {numeros}
Par: {par}
Ímpar: {impar}''')