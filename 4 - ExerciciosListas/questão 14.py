perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
resultado = 0
respostaLista = []

for i in range(0, len(perguntas)):
    print(perguntas[i])
    resposta = input('S/N? ').upper()
    while not (resposta == 'S' or resposta == 'N'):
        print('Resposta inválida')
        print(perguntas[i])
        resposta = input('S/N? ').upper()
    if resposta == 'S':
        respostaLista.append(1)
    else:
        respostaLista.append(0)

resultado = sum(respostaLista)

if resultado <= 1:
    print('Inocente')
elif resultado == 2:
    print('Suspeito')
elif resultado <= 4:
    print('Cúmplice')
elif resultado == 5:
    print('Assasino')