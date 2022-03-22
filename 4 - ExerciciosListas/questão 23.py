nomes = ['Alexandre', 'Anderson', 'Antonio', 'Carlos', 'Cesar', 'Rosemary']
espaco = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]
mb = []
porcent = []

for i in range(0, len(nomes)):
    mb.append((espaco[i]/1024)/1024)
for i in range(0, len(nomes)):
    porcent.append((mb[i] * 100)/sum(mb))
print(f'''ACME Inc.               Uso do espaço em disco pelos usuários
-------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
''')
for i in range(0, len(nomes)):
    print(f'{i + 1}    {nomes[i]:10}          {mb[i]:8.2f} MB      {porcent[i]:5.2f} %')

print(f'''
Espaço total ocupado: {sum(mb):.2f} MB
Espaço médio ocupado: {(sum(mb)/6):.2f} MB''')