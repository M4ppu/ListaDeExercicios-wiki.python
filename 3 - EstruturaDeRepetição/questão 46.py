saltos = []
nome = 1

while nome != ' ':
    nome = input('Nome: ')
    if nome == ' ':
        break
    for i in range(0, 5):
        distancia = float(input(f'Salto {i + 1}: '))
        while distancia < 0:
            print('Distância inálida')
            distancia = float(input(f'Salto {i + 1}: '))
        saltos.append(distancia)

    saltosOrganizado = sorted(saltos)
    somaSaltos = saltosOrganizado[1] + saltosOrganizado[2] + saltosOrganizado[3]
    mediaSaltos = somaSaltos/3

    print(f'''Ateta: {nome}

Primeiro salto: {saltos[0]}m
Segundo salto: {saltos[1]}m
Terceiro salto: {saltos[2]}m
Quarto salto: {saltos[3]}m
Quinto salto: {saltos[4]}m

Melhor salto: {saltosOrganizado[4]}m
Pior salto: {saltosOrganizado[0]}m
Media dos demais saltos: {mediaSaltos:.1f}m

Resultado final:
{nome}: {mediaSaltos:.1f}m''')