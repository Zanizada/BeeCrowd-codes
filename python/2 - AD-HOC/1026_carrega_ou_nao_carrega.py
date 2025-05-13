import sys

def XOR(a, b):
    total_bits = []
    bin_a = bin(a)[2:].zfill(32)
    bin_b = bin(b)[2:].zfill(32)

    for bit_a, bit_b in zip(bin_a, bin_b):
        bit_a, bit_b = int(bit_a), int(bit_b)
        if bit_a == bit_b:
            total_bits.append('0')
        else:
            total_bits.append('1')
    
    bin_c = ''.join(total_bits)
    return int(bin_c, 2)

input_data = sys.stdin.read().strip().splitlines()

for line in input_data:
    A, B = map(int, line.split())
    resultado = XOR(A, B)
    print(resultado)
