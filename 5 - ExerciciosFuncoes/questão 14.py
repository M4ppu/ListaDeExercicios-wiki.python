import itertools

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

percorreu = (list(itertools.permutations(lista)))

def quadradoSim(lista):
    linhaUm = lista[0] + lista[1] + lista[2]
    linhaDois = lista[3] + lista[4] + lista[5]
    linhaTres = lista[6] + lista[7] + lista[8]
    colunaUm = lista[0] + lista[3] + lista[6]
    colunaDois = lista[1] + lista[4] + lista[7]
    colunaTres = lista[2] + lista[5] + lista[8]
    diagonalUm = lista[0] + lista[4] + lista[8]
    diagonelDois = lista[6] + lista[4] + lista[2]
    return linhaUm == linhaDois == linhaTres == colunaUm == colunaDois == colunaTres == diagonalUm == diagonelDois

for i in percorreu:
    if quadradoSim (i):
        print(f'''{i[0]} {i[1]} {i[2]}
{i[3]} {i[4]} {i[5]}
{i[6]} {i[7]} {i[8]}
''')