num = int(input())
inicio = int(input('Começo da tabuada: '))
final = int(input('Final da tabuada: ')) + 1

while inicio > final:
    print('?????')
    inicio = int(input('Começo da tabuada: '))
    final = int(input('Final da tabuada: ')) + 1

print('Tabuada de ' + str(num))

for i in range(inicio, final):    
    print(str(num) + ' x ' + str(i) + ' = ' + str(num * i))