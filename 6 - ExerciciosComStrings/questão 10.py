num = int(input(': '))
while not (num <= 99 and num > 0):
    num = int(input(': '))

lista1 = {
    0: 'Zero',
    1: 'Um',
    2: 'Dois',
    3: 'Três',
    4: 'Quatro',
    5: 'Cinco',
    6: 'Seis',
    7: 'Sete',
    8: 'Oito',
    9: 'Nove'
}

lista2 = {
    11: 'Onze',
    12: 'Doze',
    13: 'Treze',
    14: 'Quatorze',
    15: 'Quinze',
    16: 'Dezesseis',
    17: 'Dezessete',
    18: 'Dezoito',
    19: 'Dezenove'
}

lista3 = {
    20: 'Vinte',
    30: 'Trinta',
    40: 'Quarenta',
    50: 'Cinquenta',
    60: 'Sessenta',
    70: 'Setenta',
    80: 'Oitenta',
    90: 'Noventa'
}

if (num // 10) == 0:
    print(lista1[num])
elif (num // 10) == 1:
    print(lista2[num])
else:
    decimal = (num // 10) * 10
    unidade = num % 10
    if unidade == 0:
        print(f'''{lista3[decimal]}''')
    else:
        print(f'''{lista3[decimal]} e {lista1[unidade]}''')