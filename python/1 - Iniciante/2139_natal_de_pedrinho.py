dias_por_mes = {
    1: 31, 2: 29,
    3: 31, 4: 30,
    5: 31, 6: 30,
    7: 31, 8: 31,
    9: 30, 10: 31,
    11: 30, 12: 31
}

mes, dia = map(int, input().split())

dias = 0
for meses in range(1, mes+1):
    dias += dias_por_mes[meses]
print(dias)