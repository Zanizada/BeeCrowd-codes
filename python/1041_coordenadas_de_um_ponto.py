x, y = map(float, input().split())

if x == 0 and y != 0:
    print(f'Eixo Y')
elif x != 0 and y == 0:
    print(f'Eixo X')
elif x == 0 and y == 0:
    print(f'Origem')
elif x > 0 and y > 0:
    print(f'Q1')
elif x < 0 and y > 0:
    print(f'Q2')
elif x < 0 and y < 0:
    print(f'Q3')
else:
    print(f'Q4')
