casos_teste = None
while True:
    try:
        casos_teste = int(input())
        largura, comprimento, percentual = map(int, input().split())

        area_da_casa = largura*comprimento
        area_terreno = area_da_casa/(percentual/100)
        
    except casos_teste == 0:
        break