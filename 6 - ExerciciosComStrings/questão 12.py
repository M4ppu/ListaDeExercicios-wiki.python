telefone = input('Telefone: ').replace('-', '')

if len(telefone) == 7:
    telefoneNovo = '3' + telefone
    frase = ('\nTelefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
else:
    telefoneNovo = telefone
    frase = ('')

telefoneSeparado = telefoneNovo[0: 4] + '-' + telefoneNovo[4: 8]

print(f'''Valida e corrige número de telefone
Telefone: {telefone}{frase}
Telefone corrigido sem formatação: {telefoneNovo}
Telefone corrigido com formatação: {telefoneSeparado}''')