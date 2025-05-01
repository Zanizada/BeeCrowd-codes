while True:
    N = int(input())

    if N == 0:
        break

    sequencias = []
    
    substring = None
    
    for i in range(N):
        sequencia = 1
        string = str(input())       
        if substring is None:
            substring = string
            continue
        posicao = string.find(substring)
        while True:
            if posicao != -1:
                sequencia += 1
            else:
                sequencias.append(sequencia)
                break
        maiorSequencia = max(sequencias)
        print(maiorSequencia)
