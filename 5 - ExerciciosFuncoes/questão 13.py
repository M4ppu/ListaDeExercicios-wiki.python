cima = int(input('Qnt. de cima: '))
while not (cima > 1 and cima < 20):
    print('Limite de 1 a 20')
    cima = int(input('Qnt. de cima: '))
lado = int(input('Qnt. de lado: '))
while not (lado > 1 and lado < 20):
    print('Limite de 1 a 20')
    lado = int(input('Qnt. de lado: '))

def desenhaQuadrado(cima, lado):
    tcima = '+' + '-' * (cima - 2) + '+'
    tlado = '|' + ' ' * (cima - 2) + '|'

    print(tcima)
    for i in range(lado):
        print(tlado)
    print(tcima)

desenhaQuadrado(cima, lado)