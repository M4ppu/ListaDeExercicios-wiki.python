dado = int(input(': '))

def natural (num):
    if num in [7, 11]:
        return True
    return False

def craps (num):
    if num in [2, 3, 12]:
        return True
    return False

def pontoGanhou (num1, num2):
    if num1 in [4, 5, 6, 8, 9, 10]:
        if num2 == num1:
            return True
    return False

def pontoPerdeu (num):
    if num == 7:
        return True
    return False

if natural(dado):
    print('Ganhou! "Natural"')
elif craps(dado):
    print('Perdeu :c "Craps"')
else:
    while True:
        segundoDado = int(input(': '))
        if pontoGanhou(dado, segundoDado):
            print('Ganhou! c:')
            break
        elif pontoPerdeu(segundoDado):
            print("Perdeu :'c")
            break