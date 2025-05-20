def matriz(ordem):
    matriz = [[0]*ordem for _ in range(ordem)]

    for i in range(ordem):
        for j in range(ordem):
            camada = min(i, j, ordem - 1 - i, ordem - 1 - j)
            matriz[i][j] = camada + 1

    for i in range(ordem):
        linha = f"{matriz[i][0]:>3}"
        for j in range(1, ordem):
            linha += f" {matriz[i][j]:>3}"
        print(linha)


first = True
while True:
    n = int(input())
    if n == 0:
        break
    if not first:
        print()
    else:
        first = False

    matriz(n)
