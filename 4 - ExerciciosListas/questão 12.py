alturaAlunos = []
idadeAlunos = []
result = 0

for i in range(0, 30):
    altura = float(input(f'Altura do aluno {i + 1}: '))
    while altura <= 0:
        print('Altura inválida')
        altura = float(input(f'Altura do aluno {i + 1}: '))
    alturaAlunos.append(altura)
    idade = float(input(f'Idade do aluno {i + 1}: '))
    while idade <= 0:
        print('Idade inválida')
        idade = float(input(f'Idade do aluno {i + 1}: '))
    idadeAlunos.append(idade)

media = (sum(alturaAlunos))/30

for j in range(0, len(alturaAlunos)):
    if idadeAlunos[j] > 13:
        if alturaAlunos[j] < media:
            result = result + 1

print(f'Quantidade de alunos com mais de 13 anos com a altura menor que a média: {result}')