import re

caso = 1

while True:
    try:
        numero = int(input())
        sequencia = int(input())
        numero = str(numero)
        sequencia = str(sequencia)

        casos = f"Caso #{caso}:"
        qtd_subsequencias = list(re.finditer(f"(?={re.escape(numero)})", sequencia))
        
        if qtd_subsequencias:
            qtd_subsequencias_f = f"Qtd.Subsequencias: {len(qtd_subsequencias)}"
            posicao = f"Pos: {qtd_subsequencias[-1].start() + 1}"
        else:
            qtd_subsequencias_f = f"Nao existe subsequencia"
            posicao = ""
        
        print(casos)
        print(qtd_subsequencias_f)
        if posicao:
            print(posicao)
        print()

        caso += 1

    except EOFError:
        break