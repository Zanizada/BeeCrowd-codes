def matriz(ordem):
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            camada = min(i, j, ordem - 1 - i, ordem - 1 - j)
            linha.append(str(camada + 1).rjust(3))
        print(''.join(linha))

first = True
while True:
    try:
        n = int(input())
        if n == 0:
            break
        if not first:
            print()
        else:
            first = False
        matriz(n)
    except EOFError:
        break
