n = int(input(': '))

def repetir (n):
    for i in range(1, n + 1):
        for j in range(0, i):
            print(j + 1, end = ' ')
        print()

repetir(n)