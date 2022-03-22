taxaImposto = float(input('Taxa: '))/100
custo = float(input('Valor do produto: '))

while taxaImposto < 0 or custo < 0:
    if taxaImposto < 0:
        print('Taxa negativa')
        taxaImposto = float(input('Taxa: '))/100
    if custo < 0:
        print('Custo negativo')
        custo = float(input('Valor do produto: '))

def somaImposto (tx, cu):
    return (tx * cu) + cu

print(somaImposto(taxaImposto, custo))