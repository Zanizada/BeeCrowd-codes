def tabuleiro_xadrez():
    tabuleiro = []
    for linha in range(1, 9):
        for coluna in range(1, 9):
            tabuleiro.append((linha, coluna))
    for posicao in tabuleiro:
        print(posicao)

def tabuleiro_xadrez_real():
    colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    print("  ", end="")
    for coluna in colunas:
        print(f" {coluna} ", end="")
    print()

    for linha in range(1, 9):
        print(f"{linha} ", end="")
        for _ in range(8):
            print("[ ]", end="")
        print()

# while True:
#     try:
#         X1, Y1, X2, Y2 = map(int, input().split())
        
#         if X1 == Y1 == X2 == Y2 == 0:
#             break
        
#         tabuleiro_xadrez()

#     except EOFError:
#         break

tabuleiro_xadrez_real()