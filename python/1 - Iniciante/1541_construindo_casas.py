import math

while True:
    try:
        largura, comprimento, percentual = map(int, input().split())
        
        if largura == 0 and comprimento == None and percentual == None:
            break
        
        area_da_casa = math.ceil(largura*comprimento)
        area_terreno = math.ceil(area_da_casa/(percentual/100))
        lado_terreno = math.ceil(math.sqrt(area_terreno))
        print(lado_terreno)

    except EOFError:
        break