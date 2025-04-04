T = int(input())

for _ in range(T):
    PA, PB, G1, G2 = input().split()
    PA, PB = int(PA), int(PB)
    G1, G2 = float(G1), float(G2)

    anos = 0

    while PA <= PB:
        PA += int(PA*(G1/100))
        PB += int(PB*(G2/100))
        anos += 1

        if anos > 100:
            print("Mais de 1 seculo.")
            break

    else:
        print(f"{anos} anos.")
