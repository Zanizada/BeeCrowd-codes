from rich.console import Console
from rich.table import Table

console = Console()

def tabuleiro_xadrez():
    tabuleiro = []
    for linha in range(1, 9):
        for coluna in range(1, 9):
            tabuleiro.append((linha, coluna))
    for posicao in tabuleiro:
        print(posicao)

def tabuleiro_xadrez_real():
    tabela = Table(show_header=True, header_style="bold white", show_lines=True)

    tabela.add_column(" ", style="bold")

    for letra in "A B C D E F G H".split():
        tabela.add_column(letra, justify="center")

    for linha in range(8, 0, -1):
        casas = ["[ ]" for _ in range(8)]
        tabela.add_row(str(linha), *casas)

    console.print(tabela)

# while True:
#     try:
#         X1, Y1, X2, Y2 = map(int, input().split())
        
#         if X1 == Y1 == X2 == Y2 == 0:
#             break
        
#         tabuleiro_xadrez()

#     except EOFError:
#         break

tabuleiro_xadrez_real()