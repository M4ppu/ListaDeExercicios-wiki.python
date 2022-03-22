maiorAluno = 0
menorAluno = 0
maiorAlunoN = 0
menorAlunoN = 0

for i in range(0, 10):
    numeroAluno = int(input('Número do aluno: '))
    
    while numeroAluno < 0:
        print('Número inválido')
        numeroAluno = int(input('Número do aluno: '))
    altura = float(input('Altura do aluno: '))
    
    while altura <= 0:
        print('Altura inválida')
        altura = float(input('Altura do aluno: '))

    if altura > maiorAluno:
        maiorAluno = altura
        maiorAlunoN = numeroAluno

    if i == 0:
        maiorAluno = altura
        menorAluno = altura
        maiorAlunoN = numeroAluno
        menorAlunoN = numeroAluno

    if altura < menorAluno:
        menorAluno = altura
        menorAlunoN = numeroAluno

print(f'''O aluno de número {maiorAlunoN} tem a maior altura, sendo ela: {maiorAluno}cm.
O aluno de número {menorAlunoN} tem a menor altura, sendo ela: {menorAluno}cm.''')