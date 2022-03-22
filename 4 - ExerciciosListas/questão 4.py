vogais = ['a', 'e', 'i', 'o', 'u']
letrasLista = []
qntVogal = 0

for i in range(0, 10):
    letras = input('Caractere nº ' + str(i + 1) + ': ')
    letrasLista.append(letrasLista)
    if letras in vogais:
        qntVogal = qntVogal + 1

print(f'Consoantes: {len(letrasLista) - qntVogal} ')