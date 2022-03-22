eleitores = int(input('Número de eleitores: '))
voto1 = 0
voto2 = 0
voto3 = 0

for i in range(0, eleitores):
    voto = int(input(f'''1 - Candidato 1
2 - Candidato 2
3 - candidato 3
    -------------> '''))
    while voto not in [1, 2, 3]:
        print('Candidato inválido')
        voto = int(input(f'''1 - Candidato 1
2 - Candidato 2
3 - candidato 3
    -------------> '''))
    if voto == 1:
        voto1 = voto1 + 1
    elif voto == 2:
        voto2 = voto2 + 1
    elif voto == 3:
        voto3 = voto3 + 1

print(f'''Votos no candidato 1: {voto1}
Votos no candidato 2: {voto2}
Votos no candidato 3: {voto3}''')