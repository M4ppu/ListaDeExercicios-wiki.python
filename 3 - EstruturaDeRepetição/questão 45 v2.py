gabarito = []
opcoes = ['A', 'B', 'C', 'D', 'E']
sair = False
maior = 0
menor = 0
j = 0
soma = 0

for k in range(0, 10):
    letra = input(f'Quetão {k + 1}: ').upper()
    while letra not in opcoes:
        print('Resposta inválida')
        letra = input(f'Quetão {k + 1}: ').upper()
    gabarito.append(letra)

while sair == False:

    j = j + 1
    acertos = 0
    
    for i in range(0, 10):
        resposta = input('Questão ' + str(i + 1) + ': ').upper()
        while resposta not in opcoes:
            print('Opção inválida')
            resposta = input('Questão ' + str(i + 1) + ': ').upper()
        if i == 0 and resposta == gabarito[0]:
            acertos = acertos + 1
        if i == 1 and resposta == gabarito[1]:
            acertos = acertos + 1   
        if i == 2 and resposta == gabarito[2]:
            acertos = acertos + 1
        if i == 3 and resposta == gabarito[3]:
            acertos = acertos + 1   
        if i == 4 and resposta == gabarito[4]:
            acertos = acertos + 1
        if i == 5 and resposta == gabarito[5]:
            acertos = acertos + 1   
        if i == 6 and resposta == gabarito[6]:
            acertos = acertos + 1
        if i == 7 and resposta == gabarito[7]:
            acertos = acertos + 1   
        if i == 8 and resposta == gabarito[8]:
            acertos = acertos + 1
        if i == 9 and resposta == gabarito[9]:
            acertos = acertos + 1   

    if j == 1:
        maior = acertos
        menor = acertos
    
    if acertos > maior:
        maior = acertos
    
    if acertos < menor:
        menor = acertos
    
    soma = soma + acertos

    sair1 = input('Deseja finalizar? (S/N): ').upper()
    while not (sair1 == 'S' or sair1 == 'N'):
        print('Comando inválido')
        sair1 = input('Deseja finalizar? (S/N): ').upper()
    if sair1 == 'S':
        sair = True
    elif sair1 == 'N':
        sair = False

media = soma / j

print(f'''Maior nota: {maior}
Menor nota: {menor}
Total de Alunos que utilizaram o sistema: {j}
Média das notas da turma: {media:.2f}''')