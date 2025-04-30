while True:
    D, N = map(int, input().split())
    if D == 0 and N == 0:
        V = 0
        print(V)
        break

    D = str(D)
    N = str(N)
    
    invalido = 0
    valorListado = []

    for num in N:
        if num != D:
            num = int(num)
            valorListado.append(num)
        else:
            num = int(num)

    if all(num == invalido for num in valorListado):
        V = 0
        print(V)
    else:
        V = 0
        print(V)
