temperaturaLista = []
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']


for i in range(0, 12):
    temperatura = float(input(f'Temperatura média em {mes[i]}: '))
    temperaturaLista.append(temperatura)

mediaTemperatura = (sum(temperaturaLista))/12
print()

for i in range(0, len(temperaturaLista)):
    if temperaturaLista[i] > mediaTemperatura: 
        print(f'{mes[i]}, {temperaturaLista[i]}°C')
print()