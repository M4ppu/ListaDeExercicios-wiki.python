salario = 1
abono = 0
salarioLista = []
abonoLista = []

while salario !=0:
    salario = float(input('Salário: '))
    if salario == 0:
        break
    while salario < 0:
        print('Salário inválido')
        salario = float(input('Salário: '))
    salarioLista.append(salario)

contador = 0

for i in range(0, len(salarioLista)):
    abono = salarioLista[i] * 0.2
    if abono < 100:
        abono = 100
        contador += 1
    abonoLista.append(abono)

print(f'''Projeção de Gastos com Abono
============================ 

Salário    | Abono''')


for i in range(0, len(salarioLista)):
    print(f'R$ {salarioLista[i]:7.2f} | R${abonoLista[i]:6.2f}')

print(f'''
Foram processados {len(abonoLista)} colaboradores
Total gasto com abonos: R$ {sum(abonoLista):.2f}
Valor mínimo pago a {contador} colaboradores
Maior valor de abono pago: R$ {max(abonoLista):.2f}''')