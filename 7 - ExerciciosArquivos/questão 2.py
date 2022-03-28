usuarios = open('C:/Users/luiza/Desktop/listinha/7 - ExerciciosArquivos/usuarios.txt', 'r')
nomeTodxs = {}
porcent = []

def byteParaMB(bytes):
    return ((bytes/1024)/1024)
    
def calculaPorcent(nomeTodxs):
    for i in nomeTodxs.values():
        porcent.append((i * 100)/mbTotal)
    return porcent

for line in usuarios.readlines():
    linha = line.split()
    nome = linha[0]
    bytes = int(linha[1])
    mb = byteParaMB(bytes)
    nomeTodxs[nome] = mb
    usuarios.close()
    mbTotal = sum(nomeTodxs.values())

porcent = calculaPorcent(nomeTodxs)

j = 0
relatorio = open('C:/Users/luiza/Desktop/listinha/7 - ExerciciosArquivos/relatório.txt', 'w', encoding = 'utf-8')

relatorio.write(f'''ACME Inc.               Uso do espaço em disco pelos usuários
-------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
''')
for key in nomeTodxs:
    relatorio.write(f'{j + 1}    {key:10}          {nomeTodxs[key]:8.2f} MB      {porcent[j]:5.2f} %\n')
    j += 1

relatorio.write(f'''
Espaço total ocupado: {mbTotal:.2f} MB
Espaço médio ocupado: {mbTotal/6:.2f} MB''')

relatorio.close()