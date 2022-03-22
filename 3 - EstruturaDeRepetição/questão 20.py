sair = False

while sair == False:
    fatorial = int(input())
    if fatorial <= 16:
        if fatorial < 0:
            sair = True
        else:
            result = 1
            for i in range(1, fatorial + 1):
                result = i * result
            print(result)
    else:
        print('Valor inválido')