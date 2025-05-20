def matriz(ordem):
    espaco_inicial = '  '
    for i in range(ordem):
        linha = []
        if espaco_inicial not in linha:
            linha.append(espaco_inicial)
        for j in range(ordem):
            camada = min(i, j, ordem - 1 - i, ordem - 1 - j)
            linha.append(str(camada + 1))
            if linha[0] == espaco_inicial:
                linha = [''.join(linha)]
        print('   '.join(linha))
    print()


while True:
    try:
        ordem_matriz = int(input())
        if ordem_matriz == 0:
            break
        matriz(ordem_matriz)
    except EOFError:
        break
