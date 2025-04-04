inicio = int(input().split()[1])
h1, m1, s1 = map(int, input().split(' : '))
fim = int(input().split()[1])
h2, m2, s2 = map(int, input().split(' : '))

dias = fim - inicio

if s1 <= s2:
    segundos = s2 - s1

else:
    segundos = (60 - s1) + s2
    m2 -= 1

if m1 <= m2:
    minutos = m2 - m1

else:
    minutos = (60 - m1) + m2
    h2 -= 1

if h1 < h2:
    horas = h2 - h1

elif h1 == h2 and m1 == m2 and s1 == s2:
    horas = 0
    minutos = 0
    segundos = 0
    dias += 1

else:
    horas = (24 - h1) + h2
    dias -= 1

if horas == 24:
    horas = 0
    dias += 1

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
