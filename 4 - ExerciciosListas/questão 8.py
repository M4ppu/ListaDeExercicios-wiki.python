idadeLista = []
alturaLista = []

for i in range(0, 5):
    idade = int(input(f'Idade {i + 1}: '))
    while idade < 0:
        print('Idade inválida')
        idade = int(input(f'Idade {i + 1}: '))
    idadeLista.append(idade)
    altura = float(input(f'Altura {i + 1}: '))
    while altura < 0:
        print('Altura inválida')
        altura = float(input(f'Altura {i + 1}: '))
    alturaLista.append(altura)

print(f'''Altura: {alturaLista[ : : -1]}')
{idadeLista[ : : -1]}''')