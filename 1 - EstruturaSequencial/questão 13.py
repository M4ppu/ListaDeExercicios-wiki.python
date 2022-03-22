altura = float(input('Altura: '))
sexo = input('Homem ou mulher? (H/M)').upper()

if sexo == 'H':
    pesoIdeal = (72.7 * altura) - 58 
    sexo = 'homem'
elif sexo == 'M':
    pesoIdeal = (62.1 * altura) - 44.7 
    sexo = 'mulher'

print(f'Por ser {sexo} seu peso ideal é de {pesoIdeal:.2f}Kg.')