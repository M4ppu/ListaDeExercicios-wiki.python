numeros = []

for i in range(0, 10):
    num = float(input('Número ' + str(i + 1) + (': ')))
    numeros.append(num)

print(numeros[ : : -1])