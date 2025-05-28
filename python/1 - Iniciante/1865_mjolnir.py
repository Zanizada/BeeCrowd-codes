casos_teste = int(input())

for _ in range(casos_teste):
    amigos, forca = input().split()
    forca = int(forca)

    if amigos == "Thor":
        print("Y")
    else:
        print("N")