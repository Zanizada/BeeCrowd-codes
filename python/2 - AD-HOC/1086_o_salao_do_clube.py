def processar(linhas, alvo, tabuas_cm):
    tabuas_cm.sort()
    i = 0
    j = len(tabuas_cm) - 1
    usadas = 0
    pares = 0
    usados = [False] * len(tabuas_cm)

    for idx in range(len(tabuas_cm)):
        if not usados[idx] and tabuas_cm[idx] == alvo:
            usados[idx] = True
            usadas += 1
            pares += 1
            if pares == linhas:
                return usadas

    while i < j and pares < linhas:
        while i < j and usados[i]:
            i += 1
        while i < j and usados[j]:
            j -= 1
        if i >= j:
            break
        soma = tabuas_cm[i] + tabuas_cm[j]
        if soma == alvo:
            usados[i] = usados[j] = True
            usadas += 2
            pares += 1
            i += 1
            j -= 1
        elif soma < alvo:
            i += 1
        else:
            j -= 1

    if pares == linhas:
        return usadas
    return float('inf')

while True:
    try:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        l = int(input())
        k = int(input())
        tabuas = list(map(int, input().split()))
        tabuas_cm = [x * 100 for x in tabuas]

        opcoes = []
        if (m * 100) % l == 0:
            linhas = (m * 100) // l
            comp = n * 100
            opcoes.append((linhas, comp))
        if (n * 100) % l == 0:
            linhas = (n * 100) // l
            comp = m * 100
            opcoes.append((linhas, comp))

        menor = float('inf')
        for linhas, alvo in opcoes:
            usado = processar(linhas, alvo, tabuas_cm[:])
            menor = min(menor, usado)

        print(menor if menor != float('inf') else "impossivel")
    except EOFError:
        break