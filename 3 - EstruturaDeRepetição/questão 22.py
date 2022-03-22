num = int(input('Esse número é primo? '))
i = 1
divisao = 1

while i < num - 1:
    i = i + 1
    if num % i == 0:
        print('Divisivel por: ' + str(i))
        divisao = 2

if divisao == 1:
    print('É primo')