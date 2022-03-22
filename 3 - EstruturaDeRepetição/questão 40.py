numeroAcidentes = 0
maisAcidentes = 0
menosAcidentes = 0
somaVeiculos = 0
AcidentesCidadesP = 0
qntCidadeP = 0

for i in range(0, 5):
    codigoCidade = int(input('Código da cidade: '))
    while codigoCidade < 0:
        print('Código inválido')
        codigoCidade = int(input('Código da cidade: '))
    
    numeroVeiculos = int(input('Número de veiculos: '))
    while numeroVeiculos < 0:
        print('Número inválido')
        numeroVeiculos = int(input('Número de veiculos: '))

    numeroAcidentes = int(input('Número de acidentes: '))
    while numeroAcidentes < 0:
        print('??????')
        numeroAcidentes = int(input('Número de acidentes: '))

    if i == 0:
        maisAcidentes = numeroAcidentes
        menosAcidentes = numeroAcidentes
    if numeroAcidentes > maisAcidentes:
        maisAcidentes = numeroAcidentes
    if numeroAcidentes < menosAcidentes:
        menosAcidentes = numeroAcidentes
    
    if numeroVeiculos < 2000:
        AcidentesCidadesP = AcidentesCidadesP + numeroAcidentes
        qntCidadeP = qntCidadeP + 1
    
    somaVeiculos = somaVeiculos + numeroVeiculos
if qntCidadeP == 0:
    qntCidadeP = 1

mediaVeiculos = somaVeiculos / (i + 1)
mediaAcidentesP = AcidentesCidadesP / qntCidadeP

print()
print(f'''Menor índice de acidades: {menosAcidentes}
Maior índice de acidentes: {maisAcidentes}
Média total de veiculos: {mediaVeiculos}
Média de acidentes com menos de 2000 veículos: {AcidentesCidadesP}''')