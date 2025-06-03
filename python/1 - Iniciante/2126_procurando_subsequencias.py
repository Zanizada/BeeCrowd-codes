import re

while True:
    try:
        caso = 1
        casos = f"Caso #{caso}:"
        numero = int(input())
        sequencia = int(input())
        subsequencias = list(len(re.findall(f"(?={re.escape(numero)})", sequencia)))
        posicao = subsequencias[-1].start()
        caso += 1
    except EOFError:
        break