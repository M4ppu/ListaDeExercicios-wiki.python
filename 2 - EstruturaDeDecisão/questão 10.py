turno = input('Em que turno você estuda? Matutino, vespertino ou noturno? (M, V, N) ').upper()

while not((turno == 'M') or (turno == 'V') or (turno == 'N')):
    print('Turno inválido! >:( ')
    turno = input('Fala de novo parça!')
if turno == 'M':
    print('Quem cedo madruga')
elif turno == 'V':
    print('Péssimo horario')
elif turno == 'N':
    print('Cuidado com o celular')