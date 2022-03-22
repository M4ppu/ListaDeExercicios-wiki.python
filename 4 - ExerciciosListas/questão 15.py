notaLista = []
somaAlta = 0
somaSete = 0
nota = 0
notaMaiorMedia = []
notaMenorSete = []

while nota != -1:
    nota = float(input('Nota: '))
    notaLista.append(nota)

notaLista.pop()
print(f'Total de notas: {len(notaLista)}')
print(f'Notas: {notaLista}')
print(f'Notas inversas: {notaLista[ : : -1]}')
print(f'Soma das notas: {sum(notaLista)}')
media = (sum(notaLista))/(len(notaLista))
print(f'Média da notas: {media:.2f}')

for i in range(0, len(notaLista)):
    if media < notaLista[i]:
        somaAlta += 1
        notaMaiorMedia.append(notaLista[i])
    if notaLista[i] < 7:
        somaSete += 1
        notaMenorSete.append(notaLista[i])

print(f'Quantidade de notas maiores que a média: {somaAlta}')
print(f'Nota maior que a média: {notaMaiorMedia}')
print(f'Quantidade de notas menores que sete: {somaSete}')
print(f'Notas menores que sete: {notaMenorSete}')

print('Cabô')