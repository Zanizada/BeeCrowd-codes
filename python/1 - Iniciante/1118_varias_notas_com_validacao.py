numeros = []
contador = 0

while True:
    X = float(input())

    if 1 <= X <= 10:
        contador += 1
        numeros.append(X)

        if contador == 2:
            media = sum(numeros) / 2
            print(f'media = {media:.2f}')

            while True:
                a = input('novo calculo (1-sim 2-nao)\n')

                if a.isdigit():
                    a = int(a)

                    if a == 1:
                        numeros = []
                        contador = 0
                        break

                    elif a == 2:
                        exit()

    else:
        print(f'nota invalida')
