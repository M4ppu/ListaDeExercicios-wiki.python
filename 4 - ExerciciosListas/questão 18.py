jogadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
votos = 1
porcentagemVotos = []
qntVotos = 0

while votos != 0:
    votos = int(input(': '))  
    while not (votos >= 0 and votos <= 23):
        print('Voto inválido')
        votos = int(input(': '))
    if votos == 0:
        break
    jogadores[votos - 1] += 1
    qntVotos += 1
    
totalVotos = sum(jogadores)

if qntVotos == 0:
    qntVotos = 1
for i in range(0, len(jogadores)):
    percentual = (jogadores[i] * 100) / qntVotos
    porcentagemVotos.append(percentual)

maisVotado = 0
posicaoMaisVotado = 0

for i in range(0, len(jogadores)):
    if jogadores[i] > maisVotado:
        maisVotado = jogadores[i]
        posicaoMaisVotado = i 

posicaoMaisVotado += 1

percentualMaisVotado = (maisVotado * 100) / qntVotos

print('Enquete: Quem foi o melhor jogador?')
print()

for i in range(0, len(jogadores)):
    print(f'Número do jogador {i + 1}: {jogadores[i]}')

print(f'''
Resultado da votação:

Foram computados {totalVotos} votos.

Jogador | Votos | %''')

algo = 1
contador = 0
for i in range(0, len(jogadores)):
    contador += 1
    if algo <= jogadores[i]:
        print(f'{contador}       |{jogadores[i]}      |{porcentagemVotos[i]:.2f}%')

print()
print(f'O melhor jogado foi o número {posicaoMaisVotado}, com {maisVotado} votos, correspondendo a {percentualMaisVotado:.2f}% do total de votos.')