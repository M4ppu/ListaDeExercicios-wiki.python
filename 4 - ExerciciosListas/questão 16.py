vendas = [0, 0, 0, 0, 0, 0, 0, 0, 0]
vendasBrutas = 0

while vendasBrutas != -1:
    vendasBrutas = float(input('Vendas: '))
    if vendasBrutas != -1:
        salario = (vendasBrutas * 0.09) + 200
        index = int((salario // 100) - 2)
    if index > 8:
        index = 8
    vendas[index] += 1

print(f'''$200 - $299: {vendas[0]}
$300 - $399: {vendas[1]}
$400 - $499: {vendas[2]}
$500 - $599: {vendas[3]}
$600 - $699: {vendas[4]}
$700 - $799: {vendas[5]}
$800 - $899: {vendas[6]}
$900 - $999: {vendas[7]}
$1000 em diante: {vendas[8]}''')