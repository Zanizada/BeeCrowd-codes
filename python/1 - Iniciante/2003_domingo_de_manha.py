while True:
    try:
        horas, minutos = map(int, input().split(":"))
        atraso = max(0, (horas - 7) * 60 + minutos)
        print(f"Atraso maximo: {atraso}")
        
    except EOFError:
        break
