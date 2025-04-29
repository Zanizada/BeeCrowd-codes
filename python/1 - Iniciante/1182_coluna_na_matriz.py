C = int(input())
T = input().strip()

matriz = []

for _ in range(12):
    linha = []

    for _ in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

soma = 0
for i in range(12):
    soma += matriz[i][C]

if T == "M":
    soma /= 12

print(f"{soma:.1f}")
