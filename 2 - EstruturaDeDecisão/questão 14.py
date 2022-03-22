nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

notaParcial = (nota1 + nota2)/2

print(f'''Primeira nota: {str(nota1)}
Segunda nota: {str(nota2)}
Média: {str(notaParcial)}''')

if notaParcial <= 4:
    print('E - Reprovado')
elif notaParcial <= 6:
    print('D - Reprovado')
elif notaParcial <= 7.5:
    print('C - Aprovado')
elif notaParcial <= 9:
    print('B - Aprovado')
elif notaParcial <= 10:
    print('A - Aprovado')