def temDigitosUnicos(numero):
    num_str = str(numero)

    return len(num_str) == len(set(num_str))

while True:
    N, M = int(input())

    
