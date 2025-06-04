qntd_titas, tamanho_muralhas = map(int, input().split())
tamanho_titas = input()
pequeno, medio, grande = map(int, input().split())

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

titas = [tamanhos[tita] for tita in tamanho_titas]

total_muralhas = 0
espaco_disponivel = 0

for tita in titas:
    if tita > espaco_disponivel:
        total_muralhas += 1
        espaco_disponivel = tamanho_muralhas
    espaco_disponivel -= tita

print(total_muralhas)
