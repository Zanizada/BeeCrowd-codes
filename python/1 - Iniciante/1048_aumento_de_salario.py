a = float(input())

if a >= 0 and a < 400.01:
    reajuste = a*0.15
    total = a + reajuste
    print(f'Novo salario: {total:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 15 %')
elif a >= 400.01 and a < 800.01:
    reajuste = a*0.12
    total = a + reajuste
    print(f'Novo salario: {total:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 12 %')
elif a >= 800.01 and a < 1200.01:
    reajuste = a*0.10
    total = a + reajuste
    print(f'Novo salario: {total:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 10 %')
elif a >= 1200.01 and a < 2000.01:
    reajuste = a*0.07
    total = a + reajuste
    print(f'Novo salario: {total:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 7 %')
else:
    reajuste = a*0.04
    total = a + reajuste
    print(f'Novo salario: {total:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 4 %')
