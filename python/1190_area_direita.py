O = input().strip().upper()
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
quantidade = 0

for i in range(12):
    for j in range(12):
        if j > i and i + j >= 12:
            soma += matriz[i][j]
            quantidade += 1

if O == "S":
    print(f"{soma:.1f}")
else:
    media = soma / quantidade
    print(f"{media:.1f}")
