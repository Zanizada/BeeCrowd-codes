decimal = int(input())
hexadecimal = hex(decimal)[2:]
caracteres = []
for caractere in hexadecimal:
    if 'a' <= caractere <= 'z':
        caractere = chr(ord(caractere)-32)
        caracteres.append(caractere)
    else:
        caracteres.append(caractere)

print("".join(caracteres))