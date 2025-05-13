a = 6
b = 4

def XOR(a, b):
    bin_a = bin(a)
    bin_b = bin(b)

    for bit_a, bit_b in zip(bin_a, bin_b):
        bit_a, bit_b = int(bit_a), int(bit_b)
        