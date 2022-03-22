base = int(input('Base: '))
expoenteI = int(input('Expoente: '))
expoente = expoenteI + 1
result = 1

for i in range(1, expoente):
    result = result * base

print(result)