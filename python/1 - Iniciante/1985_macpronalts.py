a = 1.50
b = 2.50
c = 3.50
d = 4.50
e = 5.50

produtos_comprados = int(input())
valor_produtos = []

for i in range(produtos_comprados):
    produto, quantidade = map(int, input().split())
    if produto == 1001:
        valor_produtos.append(quantidade*a)
    elif produto == 1002:
        valor_produtos.append(quantidade*b)
    elif produto == 1003:
        valor_produtos.append(quantidade*c)
    elif produto == 1004:
        valor_produtos.append(quantidade*d)
    elif produto == 1005:
        valor_produtos.append(quantidade*e)

valor_total = sum(valor_produtos)

print(f"{valor_total:.2f}")