preco = 1.99
valor = 1

print('Lojas Quase Dois - Tabela de preços')

for i in range(1, 51):
    valor = i * preco
    print(f'''{i} - R$ {valor:.2f}''')