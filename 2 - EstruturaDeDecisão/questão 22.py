num = float(input('Esse número é par ou impar? '))

num1 = round(num)

while num != num1:
    print('Número inválido')
    num = float(input('Só inteiro: '))
    num1 = round(num)
    
par = num%2

if par == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')