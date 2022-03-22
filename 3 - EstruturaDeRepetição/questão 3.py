nome = input('Nome: ')
idade = int(input('Idade: '))
salario = float(input('Salário: '))
sexo = input(f'''Sexo:
F - Feminino
M - Masculino
------> ''').upper()
estadoCivil = input(f'''Estado civil
S - Solteiro(a)
C - Casado(a)
V - Viúvo(a)
D - Divorciado(a)
------> ''').upper()

lista = ['S', 'C', 'V', 'D']

while len(nome) < 3:
    print('Nome inválido')
    nome = input('Nome: ')

while idade < 0 or idade > 150:
    print('Idade inválida')
    idade = int(input('Idade: '))

while salario < 0:
    print('Salário inválido')
    salario = float(input('Salário: '))

while not (sexo == 'F' or sexo == 'M'):
    print('Sexo inválido')
    sexo = input(f'''Sexo:
F - Feminino
M - Masculino
------> ''').upper()

while estadoCivil not in lista:
    print('Estado civil inválido')
    estadoCivil = input(f'''Estado civil
S - Solteiro(a)
C - Casado(a)
V - Viúvo(a)
D - Divorciado(a)
------> ''').upper()

print((nome) + ' é ' + (sexo) + ' com idade de ' + str(idade) + ' com salário de ' + str(salario) + ' e é ' + (estadoCivil))