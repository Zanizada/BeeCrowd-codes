N = int(input())

p1, p2, p3 = 2, 3, 5
medias = []

for num in range(1, N+1):
    a, b, c = map(float, input().split())
    media = ((a*p1)+(b*p2)+(c*p3))/(p1+p2+p3)
    medias.append(f'{media:.1f}')

print('\n'.join(medias))
