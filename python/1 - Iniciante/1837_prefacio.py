def divisaoTruncada (a, b):
    q = int(a / b)
    r = a - b * q

    if r < 0:
        if b > 0:
            q -= 1
            r += b
        else:
            q += 1
            r -= b

    return q, r

numeroUm, numeroDois = map(int, input().split())
quociente, resto = divisaoTruncada(numeroUm, numeroDois)
print(quociente, resto)