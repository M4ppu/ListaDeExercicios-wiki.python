numeroDaSemana = int(input('Dia da Semana: '))

diaDaSemana = [
    'Domingo', 
    'Segunda', 
    'Terça', 
    'Quarta', 
    'Quinta', 
    'Sexta', 
    'Sábado'
    ]

while numeroDaSemana not in range(0, len(diaDaSemana)+1):
    print('Valor inválido')
    numeroDaSemana = int(input('Dia da Semana: '))

print(diaDaSemana[numeroDaSemana-1])