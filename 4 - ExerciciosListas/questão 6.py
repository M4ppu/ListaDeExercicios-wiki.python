mediasSomadas = []
alunosAprovados = 0

for i in range(0, 10):
    notasAlunos = []
    print()
    print('Aluno ' + str(i + 1))
    for j in range(0, 4):
        nota = float(input('Nota ' + str(j + 1) + ': '))
        while not (nota > 0 and nota < 10):
            print('Nota inválida')
            nota = float(input('Nota ' + str(j + 1) + ': '))
        notasAlunos.append(nota)

    mediasSomadas.append(sum(notasAlunos))

for k in range(len(mediasSomadas)):
    mediaSete = mediasSomadas[k] / 4
    if mediaSete >= 7:
        alunosAprovados = alunosAprovados + 1

print()
print(f'Alunos aprovados: {alunosAprovados}')