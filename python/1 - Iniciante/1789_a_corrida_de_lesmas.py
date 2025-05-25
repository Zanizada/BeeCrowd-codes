while True:
    try:
        qntd_lesmas = int(input())
        lesmas = list(map(int, input().split()))

        lesma_rapida = max(lesmas)

        if lesma_rapida < 10:
            print("1")
        elif 10 <= lesma_rapida < 20:
            print("2")
        else:
            print("3")

    except EOFError:
        break
