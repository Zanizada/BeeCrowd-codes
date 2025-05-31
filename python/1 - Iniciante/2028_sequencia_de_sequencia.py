def sequencial(numero):
    lista = []
    for num in range(numero):
        numeracao = f"{num}", sep=" "
        lista.append(numeracao * num)
    return lista

while True:
    try:
        numero = int(input())
        print(sequencial(numero))

    except EOFError:
        break