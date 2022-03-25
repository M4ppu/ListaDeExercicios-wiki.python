import random

palavras = open('C:/Users/luiza/Desktop/listinha/6 - ExerciciosComStrings/palavras.txt', 'r')
var = palavras.readlines()
aleatoria = var[random.randint(0, len(var))].replace('\n', '').upper()
misturada = ''.join(random.sample(aleatoria,len(aleatoria)))
vezesErradas = 0
listaTentativa = []
print(f'A palavra é: {misturada}')

while vezesErradas < 6:
    palavra = input('Digite uma palavra: ').upper()
    if len(palavra) != len(aleatoria):
        print('Tamanho inválido.')
    elif not (all(i in aleatoria for i in palavra)):
        print('Letras inválidas')
    elif palavra in listaTentativa:
        print('A palavra já foi utilizada.')
    else:
        listaTentativa.append(palavra)
        if aleatoria == palavra:
            print('Você ganhou!!')
            break
        elif vezesErradas < 5:
            vezesErradas +=1
            print(f'Você errou pela {vezesErradas}ª vez.')
        else:
            vezesErradas +=1
            print(f'''-> Você errou pela {vezesErradas}ª vez. Você perdeu!
A palavra era {aleatoria}''')

palavras.close()