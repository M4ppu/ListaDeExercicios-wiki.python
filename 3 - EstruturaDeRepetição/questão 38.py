salario = float(input('Salário: '))

while salario <= 0:
    print('Você paga para tabalhar por acaso???')
    salario = float(input('Salário: '))

taxa = 0.015
anoAtual = int(input('Ano: '))

while anoAtual < 1996:
    print('Você não trabalha aqui ainda')
    anoAtual = int(input())

for i in range(1996, anoAtual + 1):
    salario = salario + (salario * taxa)
    taxa = taxa * 2

print(f'Salario em {anoAtual} de {salario:.2f} com um percentual de aumento de: {taxa}%)')
