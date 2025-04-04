numeros = []
contador = 0

while True:
    a = float(input())

    if 1 <= a <= 10:
        contador += 1
        numeros.append(a)

        if contador == 2:
            media = sum(numeros) / 2
            print(f'media = {media:.2f}')
            break
    else:
        print(f'nota invalida')
