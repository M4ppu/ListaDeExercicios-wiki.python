num = float(input(': '))

def quale (value):
    if value > 0:
        return 'P'
    elif value == 0:
        return 'nulo'
    else:
        return 'N'

print(quale(num))