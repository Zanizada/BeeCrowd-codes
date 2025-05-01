while True:
    N = int(input())
    if N == 0:
        break

    strings = [input().strip() for _ in range(N)]
    usadas = [False] * N
    maior = 0

    for i in range(N):
        if not usadas[i]:
            base = strings[i]
            grupo = [i]

            for j in range(N):
                if i != j and not usadas[j] and base in strings[j]:
                    grupo.append(j)

            for idx in grupo:
                usadas[idx] = True

            maior = max(maior, len(grupo))

    print(maior)
