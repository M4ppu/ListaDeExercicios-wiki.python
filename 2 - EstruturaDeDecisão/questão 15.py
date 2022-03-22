lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo lado: '))
lado3 = float(input('Terceiro lado: '))

if lado2 + lado3 > lado1 and lado1 + lado3 > lado2 and lado1 + lado2 > lado3:
    if lado1 == lado2 == lado3:
        print('Equilátero')

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isóceles')

    elif lado1 != lado2 != lado3 != lado1:
        print('Escaleno')

else:
    print('Não é um triângulo')