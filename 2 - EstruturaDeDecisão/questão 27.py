morango = float(input('kg de morango: '))
maca = float(input('Kg de maça: '))

if morango <= 5:
    preco1 = morango * 2.5
elif morango > 5:
    preco1 = morango * 2.2

if maca <= 5:
    preco2 = maca * 1.8
elif maca > 5:
    preco2 = maca * 1.5

totalKG = morango + maca
totalPagar = preco1 + preco2

if totalKG > 8:
    desconto = totalPagar * 0.1
elif totalPagar > 25:
    desconto = totalPagar * 0.1
else:
    desconto = 0

valorFinal = totalPagar - desconto

print('Valor total de: ' + str(valorFinal))