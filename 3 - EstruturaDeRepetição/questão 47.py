nota = []
nome = input('Nome: ')


for i in range(0, 7):
    distancia = float(input(f'Salto {i + 1}: '))
    while distancia < 0:
        print('Nota inálida')
        distancia = float(input(f'Salto {i + 1}: '))
    nota.append(distancia)

notasOrganizadas = sorted(nota)
somaNotas = notasOrganizadas[1] + notasOrganizadas[2] + notasOrganizadas[3] + notasOrganizadas[4] + notasOrganizadas[5]
mediaNotas = somaNotas/5

print(f'''Ateta: {nome}

Primeira nota: {nota[0]}
Segunda nota: {nota[1]}
Terceira nota: {nota[2]}
Quarta nota: {nota[3]}
Quinta nota: {nota[4]}
Sexta nota: {nota[5]}
Sétma nota: {nota[6]}

Resultado final:
Atleta: {nome}
Melhor nota: {notasOrganizadas[6]}
Pior nota: {notasOrganizadas[0]}
Media: {mediaNotas:.2f}''')