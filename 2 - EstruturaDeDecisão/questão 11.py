def reajuste (salario1):
    if salario1 <= 280:
        salarioNovo1 = salario1 * 1.2
        reajuste1 = salarioNovo1 - salario1
        return (salario1, salarioNovo1, 0.2, reajuste1)
    elif salario1 <= 700:
        salarioNovo2 = salario1 * 1.5
        reajuste2 = salarioNovo2 - salario1
        return (salario1, salarioNovo2, 0.5, reajuste2)
    elif salario1 <= 1500:
        salarioNovo3 = salario1 * 1.1
        reajuste3 = salarioNovo3 - salario1
        return (salario1, salarioNovo3, 0.1, reajuste3)
    elif salario1 > 1500:
        salarioNovo4 = salario1 * 1.05
        reajuste4 = salarioNovo4 - salario1
        return (salario1, salarioNovo4, 0.05, reajuste4)

def resultado (salario):
    salario, salarioNovo, porcentagem, reajusteN = reajuste(salario)
    print(f'''Salário: {str(salario)}
Porcentagem do reajuste: {str(porcentagem)}
Valor do reajuste: {str(reajusteN)}
Novo salário: {str(salarioNovo)}''')

salario = float(input('Salário atual: '))
resultado(salario)