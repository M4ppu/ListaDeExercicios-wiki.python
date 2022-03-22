import random
palavra = input()

def baralho(pal):
    lista = list(pal)
    random.shuffle(lista)

    return ''.join(lista)

print(baralho(palavra).upper())