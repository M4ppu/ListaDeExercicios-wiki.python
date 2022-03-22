divida = float(input('Valor da dívida: '))
juros = []
valorParcela = []
dividaFinal = []
parcelas = [1, 3, 6, 9, 12]

for i in parcelas:
    if i == 1:
        calculoJuros = divida * 0
        juros.append(calculoJuros)
        valorParcela.append(divida + calculoJuros)
        dividaFinal.append(divida + calculoJuros)
    elif i == 3:
        calculoJuros = divida * 0.10
        juros.append(calculoJuros)
        valorParcela.append((divida + calculoJuros)/3)
        dividaFinal.append(divida + calculoJuros)
    elif i == 6:
        calculoJuros = divida * 0.15
        juros.append(calculoJuros)
        valorParcela.append((divida + calculoJuros)/6)
        dividaFinal.append(divida + calculoJuros)
    elif i == 9:
        calculoJuros = divida * 0.20
        juros.append(calculoJuros)
        valorParcela.append((divida + calculoJuros)/9)
        dividaFinal.append(divida + calculoJuros)
    elif i == 12:
        calculoJuros = divida * 0.25
        juros.append(calculoJuros)
        valorParcela.append((divida + calculoJuros)/12)
        dividaFinal.append(divida + calculoJuros)
print('╭____________________________________________________________________╮')
print('│Qnt. Parcelas    │Valor Juros     │Valor Parcela    │V. da dívida   │')
print('│―――――――――――――――――│――――――――――――――――│―――――――――――――――――│―――――――――――――――│')

for j in range(len(parcelas)):
    print(f'''│{parcelas[j]:2.0f}x              │R$ {juros[j]:7.2f}      │R$ {valorParcela[j]:7.2f}       │R$ {dividaFinal[j]:.2f}     │''')

print('╰▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔╯')