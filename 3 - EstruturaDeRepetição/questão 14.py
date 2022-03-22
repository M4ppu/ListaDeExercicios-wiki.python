par = 0
impar = 0

for i in range(0, 10):
    num = int(input('Número: '))
    if num % 2 == 1:
        impar = impar + 1
    else:
        par = par + 1

print(f'''Quantidade de ímpar: {impar}
Quantidade de par: {par}''')