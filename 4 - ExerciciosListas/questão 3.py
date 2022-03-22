notaLista = []

for i in range(0, 4):
    nota = float(input('Nota ' + str(i + 1) + ': '))
    notaLista.append(nota)

mediaNota = (sum(notaLista))/4

print(f'''
Nota 1: {notaLista[0]}
Nota 2: {notaLista[1]}
Nota 3: {notaLista[2]}
Nota 4: {notaLista[3]}

Média: {mediaNota}''')