num1 = int(input())
num11 = num1 + 1
num2 = int(input())
soma = 0

for i in range(num11, num2): 
    print(i, end = ' ')
    soma = i + soma

print()
print('A soma é: ' + str(soma))