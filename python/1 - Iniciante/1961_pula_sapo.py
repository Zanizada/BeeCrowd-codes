altura_pulo, qntd_canos = map(int, input().split())
altura_canos = list(map(int, input().split()))

resultado = "YOU WIN"

for i in range(qntd_canos - 1):
    if abs(altura_canos[i] - altura_canos[i + 1]) > altura_pulo:
        resultado = "GAME OVER"
        break

print(resultado)
