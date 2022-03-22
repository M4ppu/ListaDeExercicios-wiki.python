populacaoA = 80000
populacaoB = 200000
anos = 0

while populacaoA < populacaoB:
    anos = anos + 1
    populacaoA = populacaoA * 1.03
    populacaoB = populacaoB * 1.015

print(anos)