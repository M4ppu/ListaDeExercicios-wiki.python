cpf = input('CPF: ')

def verificarCPF(cpf):
    while len(cpf) != 14:
        while not (cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'):
            print('Formato inválido')
            cpf = input('CPF: ')
    return cpf

def validarCPF1(cpf):
    sepradinho = cpf.split('-')
    digitos = sepradinho[0].replace('.', '')
    confimador = sepradinho[1]
    i = 10
    result = 0
    for digito in digitos:
        result = result + int(digito) * i
        i -=1
    result = (result * 10) % 11
    if result == 10:
        result = 0
    if result == int(confimador[0]):
        return True
    return False

def validarCPF2(cpf):
    sepradinho = cpf.split('-')
    digitos = sepradinho[0].replace('.', '')
    confimador = sepradinho[1]
    i = 11
    result = 0
    for digito in digitos:
        result = result + int(digito) * i
        i -=1
    result = result + (int(confimador[0]) * 2)
    result = (result * 10) % 11
    if result == 10:
        result = 0
    if result == int(confimador[1]):
        return True
    return False

if validarCPF1(cpf) and validarCPF2(cpf):
    print('CPF válido')
else:
    print('CPF inválido')