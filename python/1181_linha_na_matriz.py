L = int(input())
T = input().strip()

matriz = []

for _ in range(12):
    linha = []

    for _ in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

linha_escolhida = matriz[L]
resultado = sum(linha_escolhida)

if T == "M":
    resultado /= 12

print(f"{resultado:.1f}")
