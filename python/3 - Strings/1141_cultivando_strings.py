while True:
    N = int(input())
    if N == 0:
        break

    palavras = [input().strip() for _ in range(N)]
    usadas = [False] * N
    maior = 0

    for i in range(N):
        if not usadas[i]:
            base = palavras[i]
            grupo = []

            for j in range(N):
                if not usadas[j] and base in palavras[j]:
                    grupo.append(j)

            # Usa len(grupo) para comparar
            if len(grupo) > maior:
                maior = len(grupo)

            # Marca todos como usados
            for idx in grupo:
                usadas[idx] = True

    print(maior)
