estrelas = int(input())
carneiros = list(map(int, input().split()))

i = 0
estrelas_visitadas = [0] * estrelas

while 0 <= i < estrelas:
    if carneiros[i] > 0:
        carneiros[i] -= 1
        estrelas_visitadas[i] = 1

    if carneiros[i] % 2 != 0:
        i += 1
    else:
        i -= 1

estrelas_roubadas = sum(estrelas_visitadas)
carneiros_salvos = sum(carneiros)

print(estrelas_roubadas ,carneiros_salvos)

# estrelas = 8
# carneiros = [1, 3, 5, 7, 11, 13, 17, 19]
# i = 0
# estrelas_visitadas = [0] * estrelas
# while 0 <= 0 < estrelas: --> True
    # if carneiros[0] > 0: --> True
        # carneiros[0] -= 1 --> carneiros[0] = 0
        # estrelas_visitadas[0] = 1
    # if carneiros[0] % 2 != 0: --> False
        # i -= 1

# carneiros = [0, 3, 5, 7, 11, 13, 17, 19]
# estrelas_visitadas = [1, 0, 0, 0, 0, 0, 0, 0]

    # if carneiros[-1] > 0: --> 19 > 0 --> True
        # carneiros[-1] -= 1 --> carneiros[-1] = 18
        # estrelas_visitadas[-1] = 1
    # if carneiros[-1] % 2 != 0: --> False
        # i -= 1

# carneiros = [0, 3, 5, 7, 11, 13, 17, 18]
# estrelas_visitadas = [1, 0, 0, 0, 0, 0, 0, 1]

    # if carneiros[-2] > 0: --> 17 > 0 --> True
        # carneiros[-2] -= 1 --> carneiros[-2] = 16
        # estrelas_visitadas[-2] = 1
    # if carneiros[-2] % 2 != 0: --> False
        # i -= 1

# carneiros = [0, 3, 5, 7, 11, 13, 16, 18]
# estrelas_visitadas = [1, 0, 0, 0, 0, 0, 1, 1]

    # if carneiros[-3] > 0: --> 13 > 0 --> True
        # carneiros[-3] -= 1 --> carneiros[-3] = 12
        # estrelas_visitadas[-3] = 1
    # if carneiros[-3] % 2 != 0: --> False
        # i -= 1

# carneiros = [0, 3, 5, 7, 11, 12, 16, 18]
# estrelas_visitadas = [1, 0, 0, 0, 0, 1, 1, 1]

    # if carneiros[-4] > 0: --> 11 > 0 --> True
        # carneiros[-4] -= 1 --> carneiros[-4] = 10
        # estrelas_visitadas[-4] = 1
    # if carneiros[-4] % 2 != 0: --> False
        # i -= 1

# carneiros = [0, 3, 5, 7, 10, 12, 16, 18]
# estrelas_visitadas = [1, 0, 0, 0, 1, 1, 1, 1]

    # if carneiros[-5] > 0: --> 7 > 0 --> True
        # carneiros[-5] -= 1 --> carneiros[-5] = 6
        # estrelas_visitadas[-5] = 1
    # if carneiros[-5] % 2 != 0: --> False
        # i -= 1