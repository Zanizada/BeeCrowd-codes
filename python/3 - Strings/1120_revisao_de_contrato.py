while True:
    D, N = map(int, input().split())
    if D == 0 and N == 0:
        break

    D = str(D)
    N = str(N)
    
    valorListado = [int(num) for num in N if num != D]

    if N == D:
        print(0)

    if valorListado and not all(num == 0 for num in valorListado):
        print(int("".join(map(str, valorListado))))
    else:
        print(0)
