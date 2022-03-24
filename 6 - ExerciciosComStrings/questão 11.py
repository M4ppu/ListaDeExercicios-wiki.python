import random

palavras = open('C:/Users/luiza/Desktop/listinha/6 - ExerciciosComStrings/palavras.txt', 'r')
var = palavras.readlines()
aleatoria = var[random.randint(0, len(var))].replace('\n', '').upper()
vezesErradas = 0
lista = [False] * len(aleatoria)
listaLetras = []

while vezesErradas < 6:
    letra = input('Digite uma letra: ').upper()
    if letra in listaLetras:
        print('A letra já foi utilizada.')
    else:
        listaLetras.append(letra)
        if letra in aleatoria:
            for i in range(0, len(aleatoria)):
                if letra == aleatoria[i]:
                    lista[i] = True
            print(f'A palavra é:', end = ' ')
            for i in range(0, len(aleatoria)):
                if lista[i] == True:
                    print(aleatoria[i], end = ' ')
                else:
                    print('_', end = ' ')
            print()
        elif vezesErradas < 5:
            vezesErradas +=1
            print(f'-> Você errou pela {vezesErradas}ª vez. Tente de novo!')
        else:
            vezesErradas +=1
            print(f'''-> Você errou pela {vezesErradas}ª vez. Você perdeu!
A palavra era {aleatoria}''')
    if False not in lista:
        print('Você ganhou!')
        break