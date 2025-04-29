N = int(input())

num = 1
for _ in range(N):
    num2 = num**2
    num3 = num**3
    print(f'{num} {num2} {num3}')
    print(f'{num} {num2+1} {num3+1}')
    num += 1
