import math

def area_e_dano_da_magia(dicionario, magia, nivel):
    dano = dicionario[magia][0]
    raio = dicionario[magia][nivel]
    area = int(math.pi * (raio ** 2))
    return dano, area

casos = int(input())

magias = {
    "fire": [200, 20, 30, 50],
    "water": [300, 10, 25, 40],
    "earth": [400, 25, 55, 70],
    "air": [100, 18, 38, 60]
}

for _ in range(casos):
    largura, altura, coord_x, coord_y = map(int, input().split())
    magia, nivel, centro_x, centro_y = input()
    nivel, centro_x, centro_y = int(nivel), int(centro_x), int(centro_y)
