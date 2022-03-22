qntPessoas = int(input('Quantidade de pessoas: '))
soma = 0

for i in range(0, qntPessoas):
    idade = int(input('Idade da pessoa ' + str(i+1) + ': '))
    soma = soma + idade

result = soma / qntPessoas

if result > 0 and result <= 25:
    print('Turma jovem')
elif result <= 60:
    print('Turma adulta')
else:
    print('Turma idosa')