lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(0, 10):
    num1 = input(': ')
    num2 = input(': ')
    num3 = input(': ')
    lista1.append(num1)
    lista2.append(num2)
    lista3.append(num3)

for i in range(len(lista1)):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print(lista4)