from colorama import init, Back, Style

init()

for linha in range(8):
    for coluna in range(8):
        if (linha + coluna) % 2 == 0:
            print(Back.WHITE + '   ', end='')
        else:
            print(Back.BLACK + '   ', end='')
    print(Style.RESET_ALL)

# def tabuleiro_xadrez():
#     tabuleiro = []
#     for linha in range(1, 9):
#         for coluna in range(1, 9):
#             tabuleiro.append((linha, coluna))
#     for posicao in tabuleiro:
#         print(posicao)

# while True:
#     try:
#         X1, Y1, X2, Y2 = map(int, input().split())
        
#         if X1 == Y1 == X2 == Y2 == 0:
#             break
        
#         tabuleiro_xadrez()

#     except EOFError:
#         break