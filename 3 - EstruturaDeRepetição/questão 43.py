qntHodDog = 0
qntBauruS = 0
qntBauruOvo = 0
qntHamburguer = 0
qntXburguer = 0
qntRefri = 0
codigo = 1

while codigo > 0:
    codigo = float(input('Código do pedido: '))

    if codigo == 100:
        qntHodDog = qntHodDog + 1.20
    elif codigo == 101:
        qntBauruS = qntBauruS + 1.30
    elif codigo == 102:
        qntBauruOvo = qntBauruOvo + 1.50
    elif codigo == 103:
        qntHamburguer = qntHamburguer + 1.20
    elif codigo == 104:
        qntXburguer = qntXburguer + 1.30
    elif codigo == 105:
        qntRefri = qntRefri + 1.00
    else:
        print('Código inválido')

total = qntHodDog + qntBauruS + qntBauruOvo + qntHamburguer + qntXburguer + qntRefri

print(f'''Cachorro Quente: {qntHodDog:.2f}
Bauru Simples: {qntBauruS:.2f}
Bauru com Ovo: {qntBauruOvo:.2f}
Habúrguer: {qntHamburguer:.2f}
Cheeseburguer: {qntXburguer:.2f}
Refrigerante: {qntRefri:.2f}

Total: {total:.2f}''')