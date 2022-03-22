import random

lista = [0, 0, 0, 0, 0, 0]

for i in range(0, 100):
    num = random.randint(1, 6)
    lista[num - 1] += 1

for i in range(0, len(lista)):
    print(f'O número {i + 1} saiu {lista[i]:02.0f} vezes')