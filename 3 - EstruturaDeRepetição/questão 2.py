usuario = input('Insira o nome de usuário: ')
senha = input('Insira uma senha: ')

while usuario == senha:
    print(f'''Inválido!
Insira novamente''')
    usuario = input('Usuário: ')
    senha = input('Senha: ')

print('Usuario e senha válidos')