casos_teste = int(input())

jokenpo = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "Spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["Spock", "papel"],
    "Spock": ["tesoura", "pedra"]
}

for i in range(casos_teste):
    sheldon, raj = input().split()
    
    if sheldon in jokenpo[raj]:
        resultado = "Raj trapaceou!"
    elif raj in jokenpo[sheldon]:
        resultado = "Bazinga!"
    elif sheldon == raj:
        resultado = "De novo!"
    
    print(f"Caso #{i+1}: {resultado}")