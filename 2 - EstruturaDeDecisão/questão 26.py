tipoCombustivel = input('Álcool ou gasolina? (A/G): ').upper()

if tipoCombustivel == 'A':
    alcoolL = float(input())
    if alcoolL <= 20:
        preco = alcoolL * (1.9*0.97)
    elif alcoolL > 20:
        preco = alcoolL * (1.9*0.95)


elif tipoCombustivel == 'G':
    gasolinaL= float(input())
    if gasolinaL <= 20:
        preco = gasolinaL * (2.5*0.96)
    elif gasolinaL > 20:
        preco = gasolinaL * (2.5*0.94)

print('O valor é: ' + str(preco))