opcoes = ['A', 'B', 'C', 'D', 'E']
sair = False
maior = 0
menor = 0
j = 0
soma = 0

while sair == False:

    j = j + 1
    acertos = 0
    
    for i in range(0, 10):
        resposta = input('Questão ' + str(i + 1) + ': ').upper()
        while resposta not in opcoes:
            print('Opção inválida')
            resposta = input('Questão ' + str(i + 1) + ': ').upper()
        if i == 0 and resposta == 'A':
            acertos = acertos + 1
        if i == 1 and resposta == 'B':
            acertos = acertos + 1   
        if i == 2 and resposta == 'C':
            acertos = acertos + 1
        if i == 3 and resposta == 'D':
            acertos = acertos + 1   
        if i == 4 and resposta == 'E':
            acertos = acertos + 1
        if i == 5 and resposta == 'E':
            acertos = acertos + 1   
        if i == 6 and resposta == 'D':
            acertos = acertos + 1
        if i == 7 and resposta == 'C':
            acertos = acertos + 1   
        if i == 8 and resposta == 'B':
            acertos = acertos + 1
        if i == 9 and resposta == 'A':
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