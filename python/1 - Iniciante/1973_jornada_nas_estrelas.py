estrelas = int(input())
carneiros = list(map(int, input().split()))
carneiros_roubados = 0
estrelas_roubadas = 0
i = 0

while i in range(estrelas):
    if carneiros[i] % 2 != 0:
        carneiros_roubados += 1
        i += 1
        estrelas_roubadas += 1
        carneiros[i] = carneiros[i] - 1
    else:
        carneiros_roubados += 1
        i -= 1
        estrelas_roubadas += 1
        carneiros[i] = carneiros[i] - 1

carneiros_salvos = sum(carneiros) - carneiros_roubados

print(carneiros_salvos)