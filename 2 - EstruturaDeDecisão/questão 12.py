def salario (ganhoPorHora, HorasTrabalhadas):
    salarioBruto = ganhoPorHora * HorasTrabalhadas
    return salarioBruto

def descontoIR (salarioBruto):
    if rsalarioBruto <= 900:
        desconto0 = rsalarioBruto * 0
        return desconto0
    elif rsalarioBruto <= 1500:
        desconto5 = rsalarioBruto * 0.05
        return desconto5
    elif rsalarioBruto <= 2500:
        desconto10 = rsalarioBruto * 0.1
        return desconto10
    elif rsalarioBruto > 2500:
        desconto20 = rsalarioBruto * 0.2
        return desconto20

def descontoINSS (salarioBruto):
    inss = salarioBruto * 0.1
    return inss

def decontoFGTS (salarioBruto):
    fgts = salarioBruto * 0.11
    return fgts

def salarioFinal (salarioBruto, ir, fgts):
    salarioLiquido = salarioBruto - ir - fgts
    return salarioLiquido

gporHora = float(input('Ganho por hora: '))
horastrab = float(input('Horas trabalhadas: '))

rsalarioBruto = salario(gporHora, horastrab)
rIR = descontoIR(rsalarioBruto)
rINSS = descontoINSS(rsalarioBruto)
rFGTS = decontoFGTS(rsalarioBruto)
rSalarioLiquido = salarioFinal(rsalarioBruto, rIR, rFGTS)

print(f'''Salário Bruto : R$ {str(rsalarioBruto)}
INSS (10%) : R$ {str(rINSS)}
- IR (0-20%) : R$ {str(rIR)}
- FGTS (11%) : R$ {str(rFGTS)}
= Salário Liquido : R$ {str(rSalarioLiquido)}''')