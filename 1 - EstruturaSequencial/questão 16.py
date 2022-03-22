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

metros = float(input("Metros quadrados: "))
oquecomprarlata = quantlatas(metros)
oquegastarlata = precolata(oquecomprarlata)
oquecomprargalao = quantgalao(metros)
oquegastargalao = precogalao(oquecomprargalao)

print("Quantas latas comprar: " + str(oquecomprarlata))
print("Quantos dinheiros gastar em lata: " + str(oquegastarlata))
print("Quantas galão comprar: " + str(oquecomprargalao))
print("Quantos dinheiros gastar em galão: " + str(oquegastargalao))