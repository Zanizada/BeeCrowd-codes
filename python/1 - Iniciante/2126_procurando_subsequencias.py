while True:
    try:
        valor = int(input())
        valor = str(valor)
        numero = []
        for num in valor:
            numero.append(num)
        posicao = 0

    except EOFError:
        break