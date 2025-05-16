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
    tamanho = len(lista)
    numero_aleatorio = random.randint(0, tamanho-1)
    indice = numero_aleatorio
    menor_numero = 0
    contador = 0
    while menor_numero < area:
        while contador < tamanho:
            menor_numero =+ lista[indice]
            indice = random.randint(0, tamanho-1)
            if indice == numero_aleatorio:
                indice = random.randint(0, tamanho)
                numero_aleatorio = indice
            else:
                continue
            contador += 1


while True:
    largura, comprimento = map(int, input().split())

    if largura == 0 and comprimento == 0:
        break
    else:
        pass

    largura_tabuas_cm = int(input())
    tabuas_doadas = int(input())
    
    for i in range(tabuas_doadas):
        comprimento_tabuas = list(map(int, input().split()))

    largura_cm = conversao_m_para_cm(largura)
    comprimento_cm = conversao_m_para_cm(comprimento)
    comprimento_tabuas_cm = conversao_m_para_cm(comprimento_tabuas)
    area_do_salao_cm = largura_cm * comprimento_cm
    indice = 0
    areas_das_tabuas_cm = []
    
    while indice < tabuas_doadas:
        areas_das_tabuas_cm.append(largura_tabuas_cm * comprimento_tabuas_cm[0+indice])
        indice += 1