listaCarros = ['Clio', 'Versa', 'March', 'Civic', 'Spin']
kmL = [9.5, 12.9, 8.1, 14, 10.2]
gasolina = 2.25
precoLista = []
litrosTotal = []

for i in range(0, len(listaCarros)):
    litrosTotal.append(1000/kmL[i])
    precoLista.append((litrosTotal[i]) * gasolina)
    

print('Comparativo de Consumo de Combustível')

for i in range(0, len(listaCarros)):
    print(f'''
Veículo {i + 1}
Nome: {listaCarros[i]}
Km por litro: {kmL[i]}
''')
print('Relatório final')
for i in range(0, len(listaCarros)):
    print(f'''{i + 1} - {listaCarros[i]:6} │ {kmL[i]:4.1f} │ {litrosTotal[i]:6.2f} litros │ R$ {precoLista[i]:.2f}''')
    
print(f'O menor consumo é do {listaCarros[litrosTotal.index(min(litrosTotal))]}.')