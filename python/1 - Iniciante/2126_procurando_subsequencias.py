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
        
        if qtd_subsequencias != 0:
            qtd_subsequencias_f = f"Qtd.Subsequencias: {qtd_subsequencias}"
            subsequencias = list(len(re.findall(f"(?={re.escape(numero)})", sequencia)))
            posicao = f"Pos: {subsequencias[-1].start()}"
        else:
            qtd_subsequencias_f = f"Nao existe subsequencia"
        
        print(casos)
        print(qtd_subsequencias_f)
        print(posicao, "\n") if qtd_subsequencias != 0 else print()

        caso += 1

    except EOFError:
        break