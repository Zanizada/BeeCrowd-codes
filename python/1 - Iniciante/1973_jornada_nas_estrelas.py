estrelas = int(input())
carneiros = list(map(int, input().split()))
carneiros_roubados = 0
carneiros_salvos = sum(carneiros)

for i in range(estrelas):
    if carneiros[i] % 2 == 0:
        carneiros_roubados += 1