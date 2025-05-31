def sequencial(numero):
    lista = []
    for num in range(0, numero+1):
        num = str(num)


while True:
    try:
        numero = int(input())
        print(sequencial(numero))

    except EOFError:
        break