servidores = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votosServidores = [0, 0, 0, 0, 0, 0]
votos = 1
percentualVotos = []

print('Qual o melhor Sistema Operacional para uso em servidores?')
print()

while votos != 0:
    if votos == 0:
        break
    votos = int(input(f'''1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
---------> '''))
    while not (votos >= 0 and votos <= 6):
        print('Resposta inválida')
        votos = int(input(f'''1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
---------> '''))
    if votos != 0:
        votosServidores[votos - 1] += 1

qntVotos = sum(votosServidores)

if votos == 0:
    qntVotos = 1
for i in range(0, len(servidores)):
    percentual = (votosServidores[i] * 100) / qntVotos
    percentualVotos.append(percentual)

print('Sistema operacional | Votos | %')

for i in range(0, len(servidores)):
    print(f'{servidores[i]}    | {votosServidores[i]}  | {percentualVotos[i]:.2f}%')

print(f'Total       {qntVotos}')

maisVotado = 0
servidorMaisVotado = ''

for i in range(0, len(servidores)):
    if votosServidores[i] > maisVotado:
        maisVotado = votosServidores[i]
        servidorMaisVotado = servidores[i]

percentualMaisVotado = (maisVotado * 100) / qntVotos

print(f'O sistema operacional mais votado foi o {servidorMaisVotado}, com {maisVotado} votos, correspondendo a {percentualMaisVotado:.2f}% dos votos.')