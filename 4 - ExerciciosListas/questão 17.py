saltos = []
nome = 1

while nome != ' ':
    nome = input('Nome: ')
    if nome == ' ':
        break
    for i in range(0, 5):
        distancia = float(input(f'Salto {i + 1}: '))
        while distancia < 0:
            print('Distância inválida')
            distancia = float(input(f'Salto {i + 1}: '))
        saltos.append(distancia)

    saltosOrganizado = sorted(saltos)
    somaSaltos = sum(saltosOrganizado)
    mediaSaltos = somaSaltos/5

    print(f'''
Ateta: {nome}

Primeiro salto: {saltos[0]}m
Segundo salto: {saltos[1]}m
Terceiro salto: {saltos[2]}m
Quarto salto: {saltos[3]}m
Quinto salto: {saltos[4]}m

Resultado final:
Atleta: {nome}
Saltos: {saltos}
Media dos saltos: {mediaSaltos:.1f}m''')