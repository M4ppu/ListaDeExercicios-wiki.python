qntTurma = int(input('Número de turmas: '))
totalAlunos = 0

for i in range(0, qntTurma):
    qntAlunos = int(input('Quantidades de alunos na turma ' + str(i + 1) + ': '))
    while qntAlunos < 0 or qntAlunos > 40:
        print('Valor inválido')
        qntAlunos = int(input('Quantidades de alunos na turma ' + str(i + 1) + ': '))
    totalAlunos = totalAlunos + qntAlunos

mediaAlunos = totalAlunos/qntTurma

print('A média de alunos por turma é: ' + str(mediaAlunos))