lista1 = []
lista2 = []
lista3 = []

for i in range(0, 10):
    num1 = input(': ')
    num2 = input(': ')
    lista1.append(num1)
    lista2.append(num2)

for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)