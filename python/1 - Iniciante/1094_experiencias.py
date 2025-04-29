N = int(input())

Total = 0
coelhos = 0
ratos = 0
sapos = 0
percentual_c = percentual_r = percentual_s = 0

for num in range(1, N+1):
    Quantia, Tipo = input().split()
    Quantia = int(Quantia)
    Total += Quantia
    if Tipo == 'C':
        coelhos += Quantia
    elif Tipo == 'R':
        ratos += Quantia
    elif Tipo == 'S':
        sapos += Quantia

percentual_c = (coelhos*100)/Total
percentual_r = (ratos*100)/Total
percentual_s = (sapos*100)/Total

print(f'Total: {Total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentual_c:.2f} %')
print(f'Percentual de ratos: {percentual_r:.2f} %')
print(f'Percentual de sapos: {percentual_s:.2f} %')
