n = int(input())
fibo1 = 1
fibo2 = 1
print('1 1', end = ' ')

for i in range(0, n-2):
    aux = fibo1
    fibo1 = fibo2 + fibo1
    fibo2 = aux
    print(fibo1, end = ' ')