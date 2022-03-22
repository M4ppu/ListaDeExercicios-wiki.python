def  valorPagamento (valor, dias):
    if dias == 0:
        return(valor)
    elif dias > 0:
        return(((valor * 0.03) + valor) + ((valor * 0.001) * dias))

valorDaPrestacao = 1

while valorDaPrestacao != 0:
    valorDaPrestacao = float(input('Valor da prestação: '))
    if valorDaPrestacao == 0:
        break
    while valorDaPrestacao < 0:
        print('Valor inválido')
        valorDaPrestacao = float(input('Valor da prestação: '))
    numDiasAtraso = int(input('Número de dias em atraso: '))
    while numDiasAtraso < 0:
        print('Paga na data certa que aqui não tem desconto')
        numDiasAtraso = int(input('Número de dias em atraso: '))

    print(f'Total de: R$ {valorPagamento(valorDaPrestacao, numDiasAtraso):.2f}')