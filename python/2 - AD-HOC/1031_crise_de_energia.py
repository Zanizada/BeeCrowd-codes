import random

def josephus(lista, salto):
    indice = 0
    while len(lista) > 1:
        indice = (indice + salto - 1) % len(lista)
        lista.pop(indice)
    return lista[0]

while True:
    num_regioes = int(input())

    if num_regioes == 0:
        break

    menor_m = None
    for _ in range(1000):  # Limite de tentativas para encontrar o menor m
        m = random.randint(1, num_regioes)  # Gera um valor aleatório para m
        regioes = list(range(1, num_regioes + 1))
        resultado = josephus(regioes, m)
        if resultado == 13:
            if menor_m is None or m < menor_m:
                menor_m = m

    print(menor_m)