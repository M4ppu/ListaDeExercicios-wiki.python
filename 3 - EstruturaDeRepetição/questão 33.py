maior = 0
menor = 0
soma = 0
i = 0
num1 = 0

while num1 != 'SAIR':
    num1 = input().upper()
    if num1 == 'SAIR':
        break
    elif num1.isdigit():
        num1 = float(num1)
        
        if num1 > maior:
            maior = num1
    
        if i == 0:
            maior = num1
            menor = num1

        if num1 < menor:
            menor = num1
        
        i = i + 1
        soma = soma + num1
    else:
        print('Temperatura inexistente')

media = soma / i

print(f'''Maior nº: {maior}
Menor nº: {menor}
Média: {media}''')