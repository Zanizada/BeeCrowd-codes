def int_para_romano(numero):
    valores = [
        1000, 900, 500, 400, 100, 90,
        50, 40, 10, 9, 5, 4, 1
    ]

    simbolos = [
        "M", "CM", "D", "CD", "C", "XC",
        "L", "XL", "X", "IX", "V", "IV", "I"
    ]

    romano = ""
    for i in range(len(valores)):
        while numero >= valores[i]:
            romano += simbolos[i]
            numero -= valores[i]
    return romano

paginas = int(input())

print(int_para_romano(paginas))