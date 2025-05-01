while True:
    N = int(input())

    if N == 0:
        break

    sequenciaMaior = 1
    sequenciaAtual = 1
    substring = None

    for i in range(N):
        string = input().strip()

        if substring is None:

            substring = string
            continue

        if substring in string:
            sequenciaAtual += 1
            sequenciaMaior = max(sequenciaMaior, sequenciaAtual)
            
        else:
            sequenciaAtual = 1

        substring = string

    print(sequenciaMaior)
