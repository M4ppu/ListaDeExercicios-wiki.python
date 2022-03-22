peso = float(input('Peso: '))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print(f'''Peso de peixes: {peso}kg
Excesso: {excesso}kg
Multa de: R$ {multa:.2f}''')