def preco1Maior (primeiro, segundo, terceiro):
    if primeiro < segundo:
        if primeiro < terceiro:
            return (True)
    return (False)

def preco2Maior (primeiro, segundo, terceiro):
    if segundo < primeiro:
        if segundo < terceiro:
            return(True)
    return (False)

def preco3Maior (primeiro, segundo, terceiro):
    if terceiro < primeiro:
        if terceiro < segundo:
            return (True)
    return (False)

def resultadoMaisBarato (num1, num2, num3):
    resultMa1 = preco1Maior (num1, num2, num3)
    resultMa2 = preco2Maior (num1, num2, num3)
    resultMa3 = preco3Maior (num1, num2, num3)
    if resultMa1 == True:
        return (num1)
    if resultMa2 == True:
        return (num2)
    if resultMa3 == True:
        return (num3) 

preco1 = float(input('Primeiro preço: '))
preco2 = float(input('Segundo preço: '))
preco3 = float(input('Terceiro preço: '))

print('O mais barato é: ' + str(resultadoMaisBarato(preco1, preco2, preco3)))