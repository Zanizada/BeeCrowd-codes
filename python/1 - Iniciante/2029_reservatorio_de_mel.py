π = 3.14

while True:
    try:
        volume = float(input())
        diametro = float(input())
        raio = diametro / 2
        altura = volume / (π * (raio ** 2))
        area_base = π * (raio ** 2)
    
    except EOFError:
        break