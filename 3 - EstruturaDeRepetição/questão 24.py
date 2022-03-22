qntNotas = int(input('Quantas notas se quer calcular? '))
soma = 0

for i in range(0, qntNotas):
    nota = float(input(': '))
    soma = soma + nota

result = soma / qntNotas

print('A média é: ' + str(result))