resultados = []

while True:
    N, M = map(int, input().split())

    if N <= 0 or M <= 0:
        break

    if N > M:
        N, M = M, N

    seq = range(N, M+1)

    soma = sum(seq)

    resultados.append(f"{' '.join(map(str, seq))} Sum={soma}")

for resultado in resultados:
    print(f'{resultado}')
