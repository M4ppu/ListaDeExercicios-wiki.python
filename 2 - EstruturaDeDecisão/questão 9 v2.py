def num1Maior (primeiro, segundo, terceiro):
    if primeiro > segundo:
        if primeiro > terceiro:
            return (True)
    return (False)

def num2Maior (primeiro, segundo, terceiro):
    if segundo > primeiro:
        if segundo > terceiro:
            return(True)
    return (False)

def num3Maior (primeiro, segundo, terceiro):
    if terceiro > primeiro:
        if terceiro > segundo:
            return (True)
    return (False)

def resultadoMaior (num1, num2, num3):
    resultMa1 = num1Maior (num1, num2, num3)
    resultMa2 = num2Maior (num1, num2, num3)
    resultMa3 = num3Maior (num1, num2, num3)
    if resultMa1 == True:
        return (num1)
    if resultMa2 == True:
        return (num2)
    if resultMa3 == True:
        return (num3)    

##-----------------------------------------------------    

def num1Menor (primeiro, segundo, terceiro):
    if primeiro < segundo:
        if primeiro < terceiro:
            return (True)
    return (False)

def num2Menor (primeiro, segundo, terceiro):
    if segundo < primeiro:
        if segundo < terceiro:
            return(True)
    return (False)

def num3Menor (primeiro, segundo, terceiro):
    if terceiro < primeiro:
        if terceiro < segundo:
            return (True)
    return (False)

def resultadoMenor (num1, num2, num3):
    resultMe1 = num1Menor (num1, num2, num3)
    resultMe2 = num2Menor (num1, num2, num3)
    resultMe3 = num3Menor (num1, num2, num3)
    if resultMe1 == True:
        return (num1)
    if resultMe2 == True:
        return (num2)
    if resultMe3 == True:
        return (num3) 

##-----------------------------------------------------

def num1Meio (primeiro, segundo, terceiro):
    if primeiro > segundo:
        if primeiro < terceiro:
            return (True)
    return (False)

def num2Meio (primeiro, segundo, terceiro):
    if segundo > primeiro:
        if segundo < terceiro:
            return(True)
    return (False)

def num3Meio (primeiro, segundo, terceiro):
    if terceiro > primeiro:
        if terceiro < segundo:
            return (True)
    return (False)

def resultadoMeio (num1, num2, num3):
    resultMeo1 = num1Meio (num1, num2, num3)
    resultMeo2 = num2Meio (num1, num2, num3)
    resultMeo3 = num3Meio (num1, num2, num3)
    if resultMeo1 == True:
        return (num1)
    if resultMeo2 == True:
        return (num2)
    if resultMeo3 == True:
        return (num3) 

##-----------------------------------------------------

num1 = float(input('Primeiro: '))
num2 = float(input('Segundo: '))
num3 = float(input('Terceiro: '))

print('O maior número é: ' + str(resultadoMaior(num1, num2, num3)))
print('O do meio número é: ' + str(resultadoMeio(num1, num2, num3)))
print('O menor número é: ' + str(resultadoMenor(num1, num2, num3)))