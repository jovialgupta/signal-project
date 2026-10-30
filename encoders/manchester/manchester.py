def manchester_encode(bits):
    signal = []

    for bit in bits:
        if bit == '1':
            signal.extend([1, -1])  # High to Low
        else:
            signal.extend([-1, 1])  # Low to High

    return signal