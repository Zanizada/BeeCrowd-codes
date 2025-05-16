import random

def conversao_m_para_cm(numero=None, numeros=None):
    if numero is None and numeros is not None:
        metros = []
        for num in numeros:
            centimetros = num * 100
            metros.append(centimetros)
        return metros
    elif numeros is None and numero is not None:
        metro = numero * 100
        return metro
    else:
        raise ValueError()

def encontrar_menor_numero_possivel(lista, area):
    lista.sort(reverse=True)
    n = len(lista)
    melhor = [float('inf')]

    def backtrack(inicio, soma, usadas):
        if soma > area or usadas >= melhor[0]:
            return
        if soma == area:
            melhor[0] = min(melhor[0], usadas)
            return
        for i in range(inicio, n):
            backtrack(i + 1, soma + lista[i], usadas + 1)

    backtrack(0, 0, 0)
    return melhor[0] if melhor[0] != float('inf') else 'impossivel'


while True:
    largura, comprimento = map(int, input().split())

    if largura == 0 and comprimento == 0:
        break
    else:
        pass

    largura_tabuas_cm = int(input())
    tabuas_doadas = int(input())
    
    comprimento_tabuas = []
    for _ in range(tabuas_doadas):
        comprimento_tabuas.append(int(input()))

    largura_cm = conversao_m_para_cm(numero=largura)
    comprimento_cm = conversao_m_para_cm(numero=comprimento)
    comprimento_tabuas_cm = conversao_m_para_cm(numeros=comprimento_tabuas)
    area_do_salao_cm = largura_cm * comprimento_cm
    indice = 0
    areas_das_tabuas_cm = []
    
    while indice < tabuas_doadas:
        areas_das_tabuas_cm.append(largura_tabuas_cm * comprimento_tabuas_cm[0+indice])
        indice += 1
    
    menor_numero_possivel = encontrar_menor_numero_possivel(areas_das_tabuas_cm, area_do_salao_cm)
    print(menor_numero_possivel)