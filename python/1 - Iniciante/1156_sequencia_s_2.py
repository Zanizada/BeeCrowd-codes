S = 0
num = 1
den = 1

for _ in range(20):
    S += num / den
    num += 2
    den *= 2
    
print(f"{S:.2f}")
