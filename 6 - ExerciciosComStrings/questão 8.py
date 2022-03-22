palimdromo = input(': ').replace(' ', '')

if palimdromo == palimdromo[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')