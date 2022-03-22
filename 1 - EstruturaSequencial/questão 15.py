def salario (ganhoPorHora, HorasTrabalhadas):
    salarioBruto = ganhoPorHora * HorasTrabalhadas
    return salarioBruto

def descontoIR (salarioBruto):
    ir = salarioBruto * 0.11
    return ir

def descontoINSS (salarioBruto):
    inss = salarioBruto * 0.08
    return inss

def decontoSindicato (salarioBruto):
    sindicato = salarioBruto * 0.05
    return sindicato

def salarioFinal (salarioBruto, ir, inss, sindicato):
    salarioLiquido = salarioBruto - ir - inss - sindicato
    return salarioLiquido

gporHora = float(input())
horastrab = float(input())

rsalarioBruto = salario(gporHora, horastrab)
rIR = descontoIR(rsalarioBruto)
rINSS = descontoINSS(rsalarioBruto)
rSindicato = decontoSindicato(rsalarioBruto)
rSalarioLiquido = salarioFinal(rsalarioBruto, rIR, rINSS, rSindicato)

print(f'''Salário Bruto : R$ {str(rsalarioBruto)}
- IR (11%) : R$ {str(rIR)}
- INSS (8%) : R$ {str(rINSS)}
- Sindicato ( 5%) : R$ {str(rSindicato)}
= Salário Liquido : R$ {str(rSalarioLiquido)}''')