A, B, C, D = map(int, input().split())

if A%2 == 0:
    if C >= 0 and D >= 0:
        if B > C and D > A:
            if (C + D) > (A + B):
                print(f'Valores aceitos')
            else:
                print(f'Valores nao aceitos')
        else:
            print(f'Valores nao aceitos')
    else:
        print(f'Valores nao aceitos')
else:
    print('Valores nao aceitos')
