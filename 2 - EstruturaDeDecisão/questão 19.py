num = int(input('Diz um número menor que 1000: '))

divisao100 =  num //100
divisao10 = (num - (divisao100*100)) //10
divisao1 = num - ((divisao100*100) + (divisao10*10))

print(f'''{divisao100} Centena
{divisao10} Dezena
{divisao1} Unidade''')