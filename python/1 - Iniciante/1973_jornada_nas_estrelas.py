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