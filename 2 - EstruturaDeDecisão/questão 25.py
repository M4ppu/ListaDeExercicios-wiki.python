pergunta1 = input('Telefonou para a vítima? (S/N): ').upper()
pergunta2 = input('Esteve no local do crime? (S/N): ').upper()
pergunta3 = input('Mora perto da vítima? (S/N): ').upper()
pergunta4 = input('Devia para a vítima? (S/N): ').upper()
pergunta5 = input('Já trabalhou com a vítima? (S/N): ').upper()

result = 0

if pergunta1 == 'S':
    result = result + 1

if pergunta2 == 'S':
    result = result + 1

if pergunta3 == 'S':
    result = result + 1

if pergunta4 == 'S':
    result = result + 1

if pergunta5 == 'S':
    result = result + 1


if result <= 1:
    print('Inocente')
elif result == 2:
    print('Suspeita')
elif result <= 4:
    print('Cúmplice')
else:
    print('Assassino')