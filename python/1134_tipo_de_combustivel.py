print(f'MUITO OBRIGADO')

alcool = 0
gasolina = 0
diesel = 0

while True:
    a = int(input())

    if 1 <= a <= 4:
        
        if a == 1:
            alcool += 1
        elif a == 2:
            gasolina += 1
        elif a == 3:
            diesel += 1
        else:
            break

    else:
        continue

print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
