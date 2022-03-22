while True:

    print()
    
    valorTotal = 0
    preco = 1
    i = 0
    valores = []

    while preco != 0:
        i = i + 1
        preco = float(input('Preço ' + str(i) + ': R$ '))    
        while preco < 0:
            print('Valor inválido')
            preco = float(input('Preço ' + str(i) + ': R$ '))
        if preco > 0:        
            valorTotal = valorTotal + preco
            valores.append(preco)

    i = 0
    
    print(f'Total a pagar {valorTotal:.2f}')

    dinheiro = float(input('Valor do dinheiro recebido: '))
    troco = dinheiro - valorTotal

    while troco < 0:
        print('Falta dinheiro')
        dinheiro = float(input('Valor do dinheiro recebido: '))
        troco = dinheiro - valorTotal

    print()
    print('Lojas Tabajara')

    for j in valores:
        i = i + 1
        print(f'Produto {i}: {j:.2f}')

    print(f'''Total: {valorTotal:.2f}
Dinheiro: {dinheiro:.2f}
Troco: {troco:.2f}''')