tamanhoMB = float(input('Tamanho em MB: '))
velocidade = float(input('Velocidade em Mbps: '))

tempo = (tamanhoMB / velocidade) * 60

print(f'O tempo estimado é de {tempo:.0f} minutos.')