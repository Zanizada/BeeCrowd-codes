from collections import Counter

def resolver_caso(m, n, l, k, tabuas):
    opcoes = []
    if (m * 100) % l == 0:
        linhas = (m * 100) // l
        comprimento = n * 100
        opcoes.append((linhas, comprimento))
    if (n * 100) % l == 0:
        linhas = (n * 100) // l
        comprimento = m * 100
        opcoes.append((linhas, comprimento))

    if not opcoes:
        return 'impossivel'

    melhor = float('inf')
    tabuas_cm = [t * 100 for t in tabuas]

    for linhas, comprimento_alvo in opcoes:
        contagem = Counter(tabuas_cm)
        usadas = 0
        sucesso = True

        for _ in range(linhas):
            if contagem[comprimento_alvo] > 0:
                contagem[comprimento_alvo] -= 1
                usadas += 1
                continue

            achou = False
            for t in list(contagem.keys()):
                if contagem[t] <= 0:
                    continue
                restante = comprimento_alvo - t
                if restante < 0:
                    continue
                if restante == t:
                    if contagem[t] >= 2:
                        contagem[t] -= 2
                        usadas += 2
                        achou = True
                        break
                elif contagem[restante] > 0:
                    contagem[t] -= 1
                    contagem[restante] -= 1
                    usadas += 2
                    achou = True
                    break
            if not achou:
                sucesso = False
                break

        if sucesso:
            melhor = min(melhor, usadas)

    return melhor if melhor != float('inf') else 'impossivel'

while True:
    try:
        linha = input()
        if linha.strip() == "":
            continue
        m, n = map(int, linha.strip().split())
        if m == 0 and n == 0:
            break
        l = int(input())
        k = int(input())
        tabuas = list(map(int, input().strip().split()))
        print(resolver_caso(m, n, l, k, tabuas))
    except EOFError:
        break