num = int(input(': '))
i = 1
divisao = 1

for j in range(1, num):
    i = 1
    divisao = 1
    while i < j - 1:
        i = i + 1
        if j % i == 0:
            divisao = 2

    if divisao == 1:
        print(j, end = ' ')