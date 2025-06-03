notas = [2, 5, 10, 20, 50, 100]

while True:
    compra, cliente = map(int, input().split())
    if compra > cliente:
        valor = compra - cliente
    elif compra < cliente:
        valor = cliente - compra
    else:
        break

    tentados = set()
    for nota in notas:
        tentado = valor - nota
        if tentado in tentados:
            troco = "possible"
            break
        tentados.add(nota)
    else:
        troco = "impossible"

    print(troco)