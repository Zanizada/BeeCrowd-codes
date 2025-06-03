def raio_e_dano_da_magia(dicionario, magia, nivel):
    dano = dicionario[magia][0]
    raio = dicionario[magia][nivel]
    return dano, raio

casos = int(input())

magias = {
    "fire": [200, 20, 30, 50],
    "water": [300, 10, 25, 40],
    "earth": [400, 25, 55, 70],
    "air": [100, 18, 38, 60]
}

for _ in range(casos):
    largura, altura, x1, y1 = map(int, input().split())
    magia, nivel, centro_x, centro_y = input().split()
    nivel, centro_x, centro_y = int(nivel), int(centro_x), int(centro_y)
    dano, raio = raio_e_dano_da_magia(magias, magia, nivel)

    x2 = x1 + largura
    y2 = y1 + altura

    ex1 = centro_x - raio
    ey1 = centro_y - raio
    ex2 = centro_x + raio
    ey2 = centro_y + raio

    interseccao = not (ex2 < x1 or ex1 > x2 or ey2 < y1 or ey1 > y2)

    if interseccao:
        print(dano)
    else:
        print(0)