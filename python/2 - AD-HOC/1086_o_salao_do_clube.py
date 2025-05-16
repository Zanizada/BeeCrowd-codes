def conversao_m_para_cm(numero=None, numeros=None):
    if numero is None:
        metros = []
        for num in numeros:
            centimetros = num * 100
            metros.append(centimetros)
        return metros
    elif numeros is None:
        metro = numero * 100
        return metro

while True:
    N, M = map(int, input().split())
    L = int(input())
    K = int(input())
    for i in range(K):
        X = list(map(int, input().split()))
        