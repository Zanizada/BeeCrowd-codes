from rich.console import Console
from rich.table import Table

console = Console()

tabela = Table(show_header=True, header_style="bold", show_lines=True)
tabela.add_column(" ", style="bold")
for letra in "A B C D E F G H".split():
    tabela.add_column(letra, justify="center")

for linha in range(8, 0, -1):
    linha_casas = []
    for coluna in range(8):
        if (linha + coluna) % 2 == 0:
            cor = "on white"
        else:
            cor = "on black"
        casa = f"[{cor}]   [/{cor}]"
        linha_casas.append(casa)
    tabela.add_row(str(linha), *linha_casas)

console.print(tabela)

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