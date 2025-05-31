π = 3.14
def cilindro(volume, diametro):
    raio = diametro / 2
    altura = volume / (π * (raio ** 2))
    area = π * (raio ** 2)
    altura = f"ALTURA = {altura:.2f}"
    area = f"AREA = {area:.2f}"
    return altura, area

while True:
    try:
        volume = float(input())
        diametro = float(input())
        altura, area = cilindro(volume, diametro)
        print(altura)
        print(area)

    except EOFError:
        break