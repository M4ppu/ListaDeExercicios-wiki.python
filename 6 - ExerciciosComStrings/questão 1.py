string1 = input('1: ')
string2 = input('2: ')

print(f'''--- Compara duas strings ---
String 1: {string1}
String 2: {string2}
Tamanho de "{string1}": {len(string1)}: caracteres
Tamanho de "{string2}": {len(string2)}: caracteres''')


if len(string1) == len(string2):
    print('As duas strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')

if string1 == string2:
    print('As duas strings possuem conteúdo igual.')
else:
    print('As duas strings possuem conteúdo diferente.')