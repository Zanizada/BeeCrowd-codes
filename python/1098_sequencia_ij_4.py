I = 0.0

while I <= 2.0:
    J = 1.0 + I
    for _ in range(3):
        
        I_formatado = int(I) if I.is_integer() else I
        J_formatado = int(J) if J.is_integer() else J
        print(f'I={I_formatado} J={J_formatado}')
        J += 1
    
    I = round(I + 0.2, 1)
