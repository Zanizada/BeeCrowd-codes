a = float(input())

if a <= 2000.00:
    print(f'Isento')
else:
    imposto = 0
    
    if a >= 2000.00:
        imposto += (min(a, 3000.00) - 2000.00) * 0.08
    if a > 3000.00:
        imposto += (min(a, 4500.00) - 3000.00) * 0.18
    if a > 4500.00:
        imposto += (a - 4500.00) * 0.28

    print(f'R$ {imposto:.2f}')
