num00_25 = 0
num26_50 = 0
num51_75 = 0
num76_100 = 0
num = 0

while num >= 0 and num <= 100:
    num = int(input(': '))
    if num <= 25:
        num00_25 = num00_25 + 1
    elif num <= 50:
        num26_50 = num26_50 + 1
    elif num <= 75:
        num51_75 = num51_75 + 1
    elif num <= 100:
        num76_100 = num76_100 + 1

print(f'''Números de 00 - 25: {num00_25}
Números de 26 - 50: {num26_50}
Números de 51 - 75: {num51_75}
Números de 76 - 100: {num76_100}''')