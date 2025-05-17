def tabuleiro_xadrez():
    tabuleiro = []
    for linha in range(1, 9):
        for coluna in range(1, 9):
            tabuleiro.append((linha, coluna))

while True:
    try:
        X1, Y1, X2, Y2 = map(int, input().split())
        
        if X1 == Y1 == X2 == Y2 == 0:
            break

    except EOFError:
        break