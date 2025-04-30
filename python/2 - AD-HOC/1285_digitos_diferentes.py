import sys

def digitosUnicos(numero):
    num_str = str(numero)

    return len(num_str) == len(set(num_str))

while True:
    try:
        N, M = map(int, input().split())
        numerosValidos = 0
        for i in range(N, M+1):
            if digitosUnicos(i) == True:
                numerosValidos += 1
        print(numerosValidos)

    except EOFError:
        break
