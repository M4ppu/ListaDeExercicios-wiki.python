fatorial = int(input())
result = 1
valores = []

for i in range(1, fatorial + 1):
    result = i * result
    valores.append(i)

print(f'Fatorial de: {fatorial}')
print(f'{fatorial}! =', end = ' ')

for j in valores[ : : -1]:
    print(j, end = ' ')
    if j != 1:
        print('*', end = ' ')

print('= ' + str(result))