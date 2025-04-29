import math

N1, N2, N3, N4 = map(float, input().split())
P1 = 2
P2 = 3
P3 = 4
P4 = 1

MEDIA = ((N1*P1)+(N2*P2)+(N3*P3)+(N4*P4))/10
MEDIA_REAL = math.floor(MEDIA*10)/10
print(f'Media: {MEDIA_REAL:.1f}')

if MEDIA >= 7.0:
    print(f'Aluno aprovado.')
elif MEDIA < 5.0:
    print(f'Aluno reprovado.')
else:
    print(f'Aluno em exame.')
    A = float(input())
    print(f'Nota do exame: {A}')
    MEDIA_F = (MEDIA+A)/2
    if MEDIA_F >= 5.0:
        print(f'Aluno aprovado.')
        print(f'Media final: {MEDIA_F:.1f}')
    else:
        print(f'Aluno reprovado.')
        print(f'Media final: {MEDIA_F:.1f}')
