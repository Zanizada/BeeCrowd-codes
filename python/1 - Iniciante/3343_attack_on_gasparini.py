qntd_titas, tamanho_muralhas = map(int, input().split())
tamanho_titas = input()
pequeno, medio, grande = map(int, input().split())
total_muralhas = 1

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

titas = [tamanhos[tita] for tita in tamanho_titas]