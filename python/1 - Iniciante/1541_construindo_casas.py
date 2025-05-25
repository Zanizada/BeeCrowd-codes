import math

while True:
    entrada = input().strip()

    if entrada == "0":
        break

    A, B, C = map(int, entrada.split())

    area_casa = A * B
    area_terreno = area_casa / (C / 100)
    lado_terreno = int(math.sqrt(area_terreno))

    print(lado_terreno)