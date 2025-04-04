A, B = map(int, input().split())

if A == 1:
    P = 4
    TOTAL = B*P
    print(f'Total: R$ {TOTAL:.2f}')
else:
    if A == 2:
        P = 4.5
        TOTAL = B*P
        print(f'Total: R$ {TOTAL:.2f}')
    else:
        if A == 3:
            P = 5
            TOTAL = B*P
            print(f'Total: R$ {TOTAL:.2f}')
        else:
            if A == 4:
                P = 2
                TOTAL = B*P
                print(f'Total: R$ {TOTAL:.2f}')
            else:
                P = 1.5
                TOTAL = B*P
                print(f'Total: R$ {TOTAL:.2f}')
