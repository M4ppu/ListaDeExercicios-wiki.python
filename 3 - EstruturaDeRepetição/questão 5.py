populacaoA = float(input('População cidade A: '))
populacaoB = float(input('População cidade B: '))
anos = 0

while populacaoA < populacaoB:
    anos = anos + 1
    populacaoA = populacaoA * 1.03
    populacaoB = populacaoB * 1.015

print('Os anos necessárioa para a população de A ultrapasar B é: ' + str(anos))