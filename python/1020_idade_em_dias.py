N = int(input())
anos = N//365
N %= 365
meses = N//30
dias = N%30
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
