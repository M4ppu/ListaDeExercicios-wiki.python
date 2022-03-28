arquivo = open('C:/Users/luiza/Desktop/listinha/7 - ExerciciosArquivos/ip.txt')
validos = []
invalidos = []
def intParaStr(ip):
    for i in range(0, 4):
        ip[i] = str(ip[i])
    return ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + ip[3]

for ip in arquivo.readlines():
    ip = ip[0: -1].split('.')
    for i in range(0, 4):
        ip[i] = int(ip[i])
    if ip[0] >= 1 and ip[0] <= 126:
        if 0 <= ip[1] <= 255 and 0 <= ip[2] <= 255 and 0 <= ip[3] <= 255:
            if not (ip[1] == ip[2] == ip[3] == 0 or ip[1] == ip[2] == ip[3] == 255):
                ip = intParaStr(ip)
                validos.append(ip)
            else:
                ip = intParaStr(ip)
                invalidos.append(ip)
        else:
            ip = intParaStr(ip)
            invalidos.append(ip)
    elif ip[0] >= 128 and ip[0] <= 191:
        if 0 <= ip[1] <= 255 and 0 <= ip[2] <= 255 and 0 <= ip[3] <= 255:
            if not (ip[2] == ip [3] == 0 or ip[2] == ip [3] == 255):
                ip = intParaStr(ip)
                validos.append(ip)
            else:
                ip = intParaStr(ip)
                invalidos.append(ip)
        else:
            ip = intParaStr(ip)
            invalidos.append(ip)
    elif ip[0] >= 192 and ip[0] <= 223:
        if 0 <= ip[1] <= 255 and 0 <= ip[2] <= 255 and 1 <= ip[3] <= 254:
            ip = intParaStr(ip)
            validos.append(ip)
        else:
            ip = intParaStr(ip)
            invalidos.append(ip)
    else:
        ip = intParaStr(ip)
        invalidos.append(ip)

print('Ip válido: ' )
for i in validos:
    print(f'--> {i}') 
print('Ip inválido: ' )
for i in invalidos:
    print(f'--> {i}')

arquivo.close()