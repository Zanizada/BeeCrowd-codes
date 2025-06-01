while True:
    try:
        caso = 1
        valor = int(input())
        valor = str(valor)
        
        numero = []
        for num in valor:
            numero.append(num)

        indice = 0
        sequencia = 0
        subsequencia = 0
        while indice < len(numero):
            if numero[indice+1] == numero[indice] + 1:
                sequencia += 1
            if sequencia >= 1:
                subsequencia += 1
            indice += 1

    except EOFError:
        break