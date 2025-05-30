def macPRONALTS(produto, quantidade):
    produtos = [1001, 1002, 1003, 1004, 1005]
    valores = [1.50, 2.50, 3.50, 4.50, 5.50]
    valor_real = 0
    for i in range(len(produtos)):
        while produto == produtos[i]:
            valor_real += valores[i]
            produto -= produtos[i]
    return valor_real * quantidade

produtos_comprados = int(input())
valores_produtos = []
for i in range(produtos_comprados):
    produto, quantidade = map(int, input().split())
    valores_produtos.append(macPRONALTS(produto, quantidade))
valor_total = f"{sum(valores_produtos):.2f}"

print(valor_total)