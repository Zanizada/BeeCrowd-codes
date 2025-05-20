def matriz(ordem):
    linha = '1'
    for i in range(ordem):
        linhas = i * linha
        print(linhas, sep='   ')

while True:
    ordens_matrizes = int(input())
    
    if ordens_matrizes == 0:
        break

    matriz(ordens_matrizes)