def matriz(ordem):
    matriz = []
    for linhas_ in range(ordem):
        linha = []
        for colunas_ in range(ordem):
            linha.append(0)
        matriz.append(linha)

    for linhas in range(ordem):
        for colunas in range(ordem):
            camada = min(linhas, colunas, ordem - 1 - linhas, ordem - 1 - colunas)
            matriz[linhas][colunas] = camada + 1

    for linhas in range(ordem):
        for colunas in range(ordem):
            if colunas == 0:
                print(f"{matriz[linhas][colunas]:>3}", end='')
            else:
                print(f" {matriz[linhas][colunas]:>3}", end='')
        print()

first = True
while True:
    ordens_matrizes = int(input())
    
    if ordens_matrizes == 0:
        break

    if not first:
        print()
    else:
        first = False

    matriz(ordens_matrizes)
