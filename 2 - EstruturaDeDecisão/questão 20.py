nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira33 nota: "))

media = (nota1 + nota2 + nota3)/3

while media > 10:
    print('Nota iválida')
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira33 nota: "))
    media = (nota1 + nota2 + nota3)/3
if media == 10:
    print(f'''Média: {media}
Aprovado com distinção''')
elif media >= 7:
    print(f'''Média: {media}
Aprovado''')
else:
    print(f'''Média: {media}
Reprovado''')