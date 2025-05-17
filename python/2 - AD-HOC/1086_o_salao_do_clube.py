from collections import Counter

def conversao_m_para_cm(numero):
    if isinstance(numero, list):
        return [n * 100 for n in numero]
    else:
        return numero * 100

def resolver(c, r, largura_tabuas_cm, tabuas):
    if c % largura_tabuas_cm != 0:
        return 'impossivel'

    fileiras = c // largura_tabuas_cm
    comprimento_necessario = r

    tabuas_validas = [t for t in tabuas if t <= comprimento_necessario]

    contagem = Counter(tabuas_validas)
    usadas = 0

    usar_simples = min(contagem[comprimento_necessario], fileiras)
    usadas += usar_simples
    contagem[comprimento_necessario] -= usar_simples
    fileiras -= usar_simples

    if fileiras == 0:
        return usadas

    comprimentos = sorted(contagem.keys())
    i, j = 0, len(comprimentos) - 1

    while i <= j and fileiras > 0:
        a, b = comprimentos[i], comprimentos[j]
        if a + b < comprimento_necessario:
            i += 1
        elif a + b > comprimento_necessario:
            j -= 1
        else:
            if a == b:
                pares = contagem[a] // 2
            else:
                pares = min(contagem[a], contagem[b])

            usados_pares = min(pares, fileiras)
            usadas += usados_pares * 2
            contagem[a] -= usados_pares
            contagem[b] -= usados_pares
            fileiras -= usados_pares

            if contagem[a] == 0: i += 1
            if contagem[b] == 0: j -= 1

    return usadas if fileiras == 0 else 'impossivel'


while True:
    largura, comprimento = map(int, input().split())
    if largura == 0 and comprimento == 0:
        break

    largura_tabuas_cm = int(input())
    tabuas_doadas = int(input())
    comprimento_tabuas = list(map(int, input().split()))

    largura_cm = conversao_m_para_cm(largura)
    comprimento_cm = conversao_m_para_cm(comprimento)
    comprimento_tabuas_cm = conversao_m_para_cm(comprimento_tabuas)

    resultado = resolver(largura_cm, comprimento_cm, largura_tabuas_cm, comprimento_tabuas_cm)
    print(resultado)