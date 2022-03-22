tipoDeCarne = input(f'''1 - Filé Duplo
2 - Alcatra
3 - Picanha
------> ''')

if tipoDeCarne == '1':
    quantidade = float(input('Kg do Filé Duplo: '))
    carne = 'Filé Duplo'
    if quantidade <= 5:
        preco = quantidade * 4.9
    elif quantidade > 5:
        preco = quantidade * 5.8

elif tipoDeCarne == '2':
    quantidade = float(input('Kg da Alcatra: '))
    carne = 'Alcatra'
    if quantidade <= 5:
        preco = quantidade * 5.9
    elif quantidade > 5:
        preco = quantidade * 6.8

elif tipoDeCarne == '3':
    quantidade = float(input('Kg da Picanha: '))
    carne = 'Picanha'
    if quantidade <= 5:
        preco = quantidade * 6.9
    elif quantidade > 5:
        preco = quantidade * 7.8

tipoDePagamento = input(f'''1 - Cartão Tabajara
2 - Outro
------> ''')

if tipoDePagamento == '1':
    pagamento = 'Cartão Tabajara'
    desconto = preco * 0.05
else:
    pagamento = 'Outro'
    desconto = 0

valorFinal = preco - desconto

print(f'''Tipo da carne: {carne}
Quantidade: {quantidade}Kg
Preço total: R$ {preco}
Tipo de Pagamento: {pagamento}
Desconto: R$ {desconto}
Total a pagar: R$ {valorFinal}''')