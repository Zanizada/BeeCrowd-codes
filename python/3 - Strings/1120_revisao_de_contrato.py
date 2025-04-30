while True:
    D, N = map(int, input().split())
    if D == 0 and N == 0:
        print(0)
        break

    D = str(D)
    N = str(N)
    
    valorListado = [int(num) for num in N if num != D]

    if all(num == 0 for num in valorListado):
        print(0)
    else:
        print("".join(map(str, valorListado)))
