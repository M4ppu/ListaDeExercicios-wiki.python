cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0
votos = 1

while votos > 0:
    votos = int(input(f'''1 - José
2 - João
3 - Enzo
4 - July
5 - Voto nulo
6 - Voto em branco
------------> '''))
    if votos != 0:
        if votos == 1:
            cand1 = cand1 + 1
        elif votos == 2:
            cand2 = cand2 + 1
        elif votos == 3:
            cand3 = cand3 + 1
        elif votos == 4:
            cand4 = cand4 + 1
        elif votos == 5:
            nulo = nulo + 1
        elif votos == 6:
            branco = branco + 1
        else:
            print(f'Voto inválido')

totalVotos = cand1 + cand2 + cand3 + cand4 + nulo + branco
percentagemNulo = (nulo / totalVotos) * 100
percentagemBranco = (branco / totalVotos) * 100

print(f'''José {cand1} votos
João {cand2} votos
Enzo {cand3} votos
July {cand4} votos

Votos nulos: {nulo}
Votos em branco: {branco}
Percentagem nulos: {percentagemNulo:.2f} %
Percentagem brancos: {percentagemBranco:.2f} %''')