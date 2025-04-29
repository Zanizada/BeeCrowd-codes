while True:
    X = int(input())

    if X != 0:
        numeros = list(range(1, X+1))
        print(" ".join(map(str, numeros)))
            
    else:
        break
