def sequencial(numero):
    lista = []
    quantidade = 0

    for num in range(0, numero + 1):
        parte = [str(num)] * num
        lista.extend(parte)
        quantidade += num

    lista = ["0"] + lista
    quantidade += 1
    return lista, quantidade

indice = 1
while True:
    try:
        numero = int(input())
        sequencia, quantidade = sequencial(numero)

        if quantidade == 1:
            numeros = "numero"

        else:
            numeros = "numeros"
        print(f"Caso {indice}: {quantidade} {numeros}")
        print(" ".join(sequencia))
        print()
        indice += 1

    except EOFError:
        break
