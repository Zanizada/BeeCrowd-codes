qntd_titas, tamanho_muralhas = map(int, input().split())
tamanho_titas = input()
pequeno, medio, grande = map(int, input().split())

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

titas = []
for tita in tamanho_titas:
    tita = tamanhos[tita]
    titas.append(tita)

total_tamanho_titas = sum(titas)
total_muralhas = 1
if tamanho_muralhas < total_tamanho_titas:
    total_muralhas = 2
    tamanho_muralhas += tamanho_muralhas
    while tamanho_muralhas < total_tamanho_titas:
        tamanho_muralhas += tamanho_muralhas
        total_muralhas += 1

print(total_muralhas)

# muralha de 20 metros, 8 titãs, 5 de 10 metros, 1 de 8 metros, 2 de 3 metros:
# 1ª muralha: 20 - 20 = 0
# 2ª muralha: 20 - 20 = 0
# 3ª muralha: 20 - 18 = 2
# 4ª muralha: 20 - 6  = 4