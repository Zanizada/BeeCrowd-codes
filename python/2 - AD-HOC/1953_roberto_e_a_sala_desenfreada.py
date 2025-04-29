qntdDeAlunos = int(input())
EPR = 0
EHD = 0
INTRUSOS = 0

for i in range(qntdDeAlunos):
    matricula, curso = input().split();
    matricula = int(matricula);

    if curso == 'EPR':
            EPR += 1
    elif curso == 'EHD':
            EHD += 1
    else:
        INTRUSOS += 1

print(f'EPR: {EPR}')
print(f'EHD: {EHD}')
print(f'INTRUSOS: {INTRUSOS}')
