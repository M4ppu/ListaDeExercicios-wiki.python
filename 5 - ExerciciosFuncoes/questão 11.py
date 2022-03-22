from datetime import datetime

dma = input('Dia, mês e ano (DD/MM/AAAA): ')
meses = {
    '01':'Janeiro',
    '02':'Fevereiro',
    '03':'Março',
    '04':'Abril',
    '05':'Maio',
    '06':'Junho',
    '07':'Julho',
    '08':'Agosto',
    '09':'Setembro',
    '10':'Outubro',
    '11':'Novembro',
    '12':'Dezembro'
}

def validaData (data):
    try: 
        aaa = datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def convertData (data):
    if validaData(data):
        sepradinho = data.split('/')
        if len(sepradinho[1]) == 1:
            sepradinho[1] = '0' + sepradinho[1]
        if len(sepradinho[0]) == 1:
            sepradinho[0] = '0' + sepradinho[0]
        return sepradinho[0] + ' de ' + meses[sepradinho[1]] + ' de ' + sepradinho[2]
    return None

print(convertData(dma))