while True:
    D, N = map(int, input().split())
    D, N = str(D), str(N)

    if D == '0' and N == '0':
        break

    resultado = N.replace(D, '')

    if resultado == '':
        print(0)
    else:
        print(int(resultado))
