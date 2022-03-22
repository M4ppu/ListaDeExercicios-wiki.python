preco = 0.18
valor = 1

print(f'''Preço do pão: R$ {preco}
Panificadora Pão de Ontem - Tabela de preços''')

for i in range(1, 51):
    valor = i * preco
    print(f'''{i} - R$ {valor:.2f}''')