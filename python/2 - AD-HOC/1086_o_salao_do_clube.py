def conversao_m_para_cm(numero=None, numeros=None):
    if numero is None and numeros is not None:
        metros = []
        for num in numeros:
            centimetros = num * 100
            metros.append(centimetros)
        return metros
    elif numeros is None and numero is not None:
        metro = numero * 100
        return metro
    else:
        raise ValueError()

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    else:
        pass

    L = int(input())
    K = int(input())
    
    for i in range(K):
        X = list(map(int, input().split()))

    N = conversao_m_para_cm(N)
    M = conversao_m_para_cm(N)
    comprimento_tabuas = conversao_m_para_cm(X)
