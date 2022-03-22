mouseLista = [0, 0, 0, 0]
mouse = 1
necessidades = ['Necessita da esfera', 'Necessita de limpeza', 'Necessita troca do cabo ou conector', 'Quebrado ou inutilizado']
while mouse != 0:
    mouse = int(input(f'''1 - Esfera
2 - Limpeza
3 - Troca do cabo ou conector
4 - Quebrado ou inutilizado
------> '''))
    while not (mouse >= 0 and mouse <= 4):
        print('Comando inválido')
        mouse = int(input(f'''1 - Esfera
2 - Limpeza
3 - Troca do cabo ou conector
4 - Quebrado ou inutilizado
------> '''))
    if mouse == 0:
        break
    mouseLista[mouse - 1] += 1
print(f'''
Quantidade de mouses: {sum(mouseLista)}

Situação                               | Quantidade | Percentual''')
for i in range(0, len(mouseLista)):
    print(f'{i + 1}- {necessidades[i]:35} | {mouseLista[i]:10} | {(mouseLista[i] * 100)/sum(mouseLista):8.2f} %')