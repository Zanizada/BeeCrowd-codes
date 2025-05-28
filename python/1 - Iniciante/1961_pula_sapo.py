altura_pulo, qntd_canos = map(int, input().split())
altura_canos = list(map(int, input().split()))

indice = 0
while indice < len(altura_canos):
    cano_atual = altura_canos[0+indice]
    proximo_cano = altura_canos[1+indice]
