while True:
    N = int(input())

    if N == 0:
        break

    sequencias = []
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
        else:
            sequencias.append(sequenciaAtual)
            sequenciaAtual = 1

        substring = string
    
    sequencias.append(sequenciaAtual)
    sequenciaMaior = max(sequencias)

    print(sequenciaMaior)
