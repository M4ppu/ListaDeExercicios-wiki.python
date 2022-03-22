qntCD = int(input('Número de CDs: '))
totalGasto = 0

for i in range(0, qntCD):
    valorCD = float(input('Valor pago no CD ' + str(i + 1) + ': '))
    while valorCD < 0:
        print('Valor inválido')
        valorCD = float(input('Valor pago no CD ' + str(i + 1) + ': '))
    totalGasto = totalGasto + valorCD

mediaGasta = totalGasto/qntCD

print(f'''Você gastou {totalGasto} em CDs.
A média gasta por CD foi de {round(mediaGasta, 2)}.''')