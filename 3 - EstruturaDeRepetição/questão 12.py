num = int(input())

while num < 0 or num > 10:
    print('Número inválido')
    num = int(input())

print('Tabuada de ' + str(num))

for i in range(1, 11):    
    print(str(num) + ' x ' + str(i) + ' = ' + str(num * i))