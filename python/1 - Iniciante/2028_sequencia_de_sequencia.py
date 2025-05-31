def sequencial(numero):
    lista = ["0"]
    quantidade = 0
    for num in range(0, numero+1):
        nums = str(num)
        numeracao = " ".join(nums * num)
        lista.append(numeracao)
        quantidade += num
    del lista[1]
    return lista, quantidade
while True:
    try:
        numero = int(input())
        print(sequencial(numero))

    except EOFError:
        break