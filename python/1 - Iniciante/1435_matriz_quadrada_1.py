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

    for i in range(ordem):
        for j in range(ordem):
            if j == 0:
                # Sem espaço no início
                print(f"{matriz[i][j]:>3}", end='')
            else:
                # Um espaço entre os números
                print(f" {matriz[i][j]:>3}", end='')
        print()

# Loop para ler entradas e processar cada matriz
first = True
while True:
    ordens_matrizes = int(input())
    
    if ordens_matrizes == 0:
        break

    if not first:
        print()  # Linha em branco entre as matrizes
    else:
        first = False

    matriz(ordens_matrizes)
