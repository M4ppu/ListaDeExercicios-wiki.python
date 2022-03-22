num1 = float(input('Primeiro: '))
num2 = float(input('Segundo: '))
num3 = float(input('Terceiro: '))

if num1 > num2 > num3:
    print('O primeiro é maior')
    if num1 > num3 > num2:
        print('O primeiro é maior')
elif num2 > num1> num3:
    print('O segundo é maior')
    if num2 > num3 > num1:
        print('O segundo é maior')
elif num3 > num1 > num2:
    print('O terceiro é maior')
    if num3 > num2 > num1:
        print('O terceiro é maior')