estrelas = int(input())
carneiros = list(map(int, input().split()))

i = 0
estrelas_visitadas = [0] * estrelas

while True:
    if carneiros[i] > 0:
        carneiros[i] -= 1
        estrelas_visitadas[i] = 1

    if carneiros[i] % 2 != 0:
        i += 1
    else:
        i -= 1
    
    if i < -8 or i > 8:
        break

estrelas_roubadas = sum(estrelas_visitadas)
carneiros_salvos = sum(carneiros)

print(estrelas_roubadas ,carneiros_salvos)

# estrelas = 8
# carneiros = [1, 3, 5, 7, 11, 13, 16, 19]
# i = 0
# estrelas_visitadas = [0] * estrelas
# while 0 <= i < estrelas: --> True
    # if carneiros[0] > 0: --> True
        # carneiros[0] -= 1 --> carneiros[0] = 0
        # estrelas_visitadas[0] = 1
    # if carneiros[0] % 2 != 0: --> False
        # i -= 1

# carneiros = [0, 3, 5, 7, 11, 13, 16, 19]
# estrelas_visitadas = [1, 0, 0, 0, 0, 0, 0, 0]

    # if carneiros[-1] > 0: --> 19 > 0 --> True
        # carneiros[-1] -= 1 --> carneiros[-1] = 18
        # estrelas_visitadas[-1] = 1
    # if carneiros[-1] % 2 != 0: --> False
        # i -= 1

# carneiros = [0, 3, 5, 7, 11, 13, 16, 18]
# estrelas_visitadas = [1, 0, 0, 0, 0, 0, 0, 1]

    # if carneiros[-2] > 0: --> 16 > 0 --> True
        # carneiros[-2] -= 1 --> carneiros[-2] = 15
        # estrelas_visitadas[-2] = 1
    # if carneiros[-2] % 2 != 0: --> True
        # i += 1

# carneiros = [0, 3, 5, 7, 11, 13, 15, 18]
# estrelas_visitadas = [1, 0, 0, 0, 0, 0, 1, 1]

    # if carneiros[-2] > 0: --> 16 > 0 --> True
        # carneiros[-2] -= 1 --> carneiros[-2] = 15
        # estrelas_visitadas[-2] = 1
    # if carneiros[-2] % 2 != 0: --> True
        # i += 1