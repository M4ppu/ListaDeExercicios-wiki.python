frase = input(': ')
contEspaco = 0
contVogal = 0
vogal = ['a', 'e', 'i', 'o', 'u']

for i in frase:
    if i == ' ':
        contEspaco +=1
    if i in vogal:
        contVogal +=1

print(f'''Nº de espaço: {contEspaco}
Nº de vogal: {contVogal}''')