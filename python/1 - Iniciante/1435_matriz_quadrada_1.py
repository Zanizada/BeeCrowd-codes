def matriz(ordem):
    espaço_inicial = '  '
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            camada = min(i, j, ordem - 1 - i, ordem - 1 - j)
            linha.append(str(camada + 1))
        print('   '.join(linha))

while True:
    try:
        n = int(input())
        if n == 0:
            break
        matriz(n)
        print()
    except EOFError:
        break
