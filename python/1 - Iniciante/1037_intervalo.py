N = float(input())
if N >= 0 and N <= 50.0000:
    if N >= 0 and N <= 25.0000:
        print(f'Intervalo [0,25]')
    else:
        print(f'Intervalo (25,50]')
elif N >= 50.00001 and N<= 100.0000:
    if N >= 50.00001 and N <= 75.0000:
        print(f'Intervalo (50,75]')
    else:
        print(f'Intervalo (75,100]')
else:
    print(f'Fora de intervalo')
