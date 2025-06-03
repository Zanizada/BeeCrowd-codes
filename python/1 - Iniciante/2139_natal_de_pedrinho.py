meses = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
}

dias = {
    "janeiro": 31,
    "fevereiro": 60,
    "março": 91,
    "abril": 121,
    "maio": 152,
    "junho": 182,
    "julho": 213,
    "agosto": 244,
    "setembro": 274,
    "outubro": 305,
    "novembro": 335,
    "dezembro": 366
}

natal = False
while True:
    try:
        mes, dia = map(int, input().split())
        
        if meses[12] and dia == 25:
            natal = True

    except EOFError:
        break