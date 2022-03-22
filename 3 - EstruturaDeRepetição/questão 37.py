maiorAltura = 0
menorAltura = 0
maiorPeso = 0
menorPeso = 0
somaAltura = 0
somaPeso = 0
i = 0
codigo = 1

while codigo != 0:
    codigo = int(input('Código: '))
    if codigo != 0:
        altura = float(input('Altura: '))
        peso = float(input('Peso: '))
        while codigo < 0 or altura < 0 or peso <0:
            if codigo < 0:
                print('Código inválido')
                codigo = int(input('Código: '))
            if altura <0:
                print('Altura inválida')
                altura = float(input('Altura: '))
            if peso < 0:
                print('Peso inválido')
                peso = float(input('Peso: '))

        if altura > maiorAltura:
            maiorAltura = altura
        if i == 0:
            maiorAltura = altura
            menorAltura = altura
        if altura < menorAltura:
            menorAltura = altura
        somaAltura = somaAltura + altura

        if peso > maiorPeso:
            maiorPeso = peso
        if i == 0:
            maiorPeso = peso
            menorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
        somaPeso = somaPeso + peso

        i = i + 1

mediaAltura = somaAltura / i
mediaPeso = somaPeso / i

print(f'''Maior peso: {maiorPeso}
Menor peso: {menorPeso}
Maior altura: {maiorAltura}
Menor altura: {menorAltura}
Média das alturas: {mediaAltura}
Média dos pesos: {mediaPeso}''')