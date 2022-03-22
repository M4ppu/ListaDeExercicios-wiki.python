def convert (hr, min):
    if hr == 12:
        return hr, min, 'P'
    elif hr > 12:
        return hr - 12, min, 'P'
    return hr, min, 'A'

def relogio (hr, min, turno):
    if turno == 'P':
        print(f'{hr}:{min} P.M.')
    elif turno == 'A':
        print(f'{hr}:{min} A.M.')

while True:
    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))
    while horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        if not (horas > 0 and minutos < 23):
            print('Hora negativa ou maior que 23')
            horas = int(input('Horas: '))
        if not (minutos > 0 and minutos < 59):
            print('Minuto negativo ou maior que 59')
            minutos = int(input('Minutos: '))
    horas, minutos, periodo = convert(horas, minutos)
    relogio(horas, minutos, periodo)