import math

def quantlatas (metrosQuadrados):
    quantidadeLatas = math.ceil((metrosQuadrados/6)/18)
    return quantidadeLatas

def quantgalao (metrosQuadrados):
    quantidadeGalao = math.ceil((metrosQuadrados/6)/3.6)
    return quantidadeGalao

def precolata (quantidadeLatas):
    totallata = quantidadeLatas * 80
    return totallata

def precogalao (quantidadeGalao):
    totalgalao = quantidadeGalao * 25
    return totalgalao

def quantlataegalao (metros):
    calculo1 = round((metros/6)/18)
    metrosrestantes = metros - (calculo1 * 18 * 6)
    calculo2 = (math.ceil((metrosrestantes/6)/3.6))
    return (calculo1, calculo2)

metros = float(input("Metros quadrados: "))
oquecomprarlata = quantlatas(metros)
oquegastarlata = precolata(oquecomprarlata)
oquecomprargalao = quantgalao(metros)
oquegastargalao = precogalao(oquecomprargalao)

print("Quantas latas comprar: " + str(oquecomprarlata))
print("Quantos dinheiros gastar em lata: " + str(oquegastarlata))
print("Quantas galão comprar: " + str(oquecomprargalao))
print("Quantos dinheiros gastar em galão: " + str(oquegastargalao))
print("Quantidade de latas e galões: " + str(quantlataegalao(metros)))