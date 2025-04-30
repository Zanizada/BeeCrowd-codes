while True:
    N = int(input())

    if N == 0:
        break
    
    sequencias = []
    
    for i in range(N):
        sequencia = 1
        foto = str(input())
        while True:
            if texto.find(foto) != -1:
                sequencia += 1
            else:
                sequencias.append(sequencia)
                break
