casos = int(input())

for i in range(casos):
    palavra = input()
    tempo = 0
    for letra in palavra:
        tempo += 0.01
    print(f"{tempo:.2f}")