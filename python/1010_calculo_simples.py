_, N1, V1 = input().split()
N1 = int(N1)
V1 = float(V1)

_, N2, V2 = input().split()
N2 = int(N2)
V2 = float(V2)

VT = (N1 * V1) + (N2 * V2)

print(f'VALOR A PAGAR: R$ {VT:.2f}')
