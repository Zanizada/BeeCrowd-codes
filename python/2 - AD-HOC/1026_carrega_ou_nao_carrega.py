a = 6
b = 4

def XOR(a, b):
    bits_c = 0
    total_bits = []
    bin_a = bin(a)[2:].zfill(32)
    bin_b = bin(b)[2:].zfill(32)

    for bit_a, bit_b in zip(bin_a, bin_b):
        bit_a, bit_b = int(bit_a), int(bit_b)
        if bit_a == bit_b:
            total_bits.append(0)
        else:
            total_bits.append(1)
    bits_c.join(total_bits)
    bin_c = str(bits_c)
    int_c = int(bin_c, 2)
    return int_c

try:
    A = int(input())
    B = int(input())
    resultado = XOR(A, B)
    print(resultado)

except EOFError:
