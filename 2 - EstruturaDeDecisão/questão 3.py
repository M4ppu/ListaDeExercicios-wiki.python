letraFouM = input('Manda F ou M: ')

letraFouM = letraFouM.upper()

while not((letraFouM == 'F') or (letraFouM == 'M')):
    print('Sexo inválido! >:(')
    letraFouM = input('Fala de novo parça!')
if letraFouM == 'F':
    print('Esse é feminino!!')
else:
    print('Isso é masculino')