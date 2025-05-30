def macPRONALTS(produto, quantidade):
    produtos = {
        1001: 1.50,
        1002: 2.50,
        1003: 3.50,
        1004: 4.50,
        1005: 5.50
    }
    return produtos[produto] * quantidade

produtosComprados = int(input())
valorTotal = 0
for _ in range(produtosComprados):
    produto, quantidade = map(int, input().split())
    valorTotal += macPRONALTS(produto, quantidade)
print(f"{valorTotal:.2f}")