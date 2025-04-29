A, B = map(int, input().split())
if A%B == 0 or B%A == 0:
    print(f'Sao Multiplos')
else:
    print(f'Nao sao Multiplos')
