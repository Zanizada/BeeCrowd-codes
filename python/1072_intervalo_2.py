N = int(input())

intervalo = range(10, 20)

contador_in = 0
contador_out = 0

for num in range(1, N + 1):
    X = int(input())
    if X in intervalo:
        contador_in += 1
        
    else:
        contador_out += 1

print(f'{contador_in} in')
print(f'{contador_out} out')
