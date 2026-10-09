def manchester_encode(bits):
    signal = []

    for bit in bits:
        if bit == '1':
            signal.extend([1, -1])
        elif bit == '0':
            signal.extend([-1, 1])
        else:
            raise ValueError("Bits must contain only 0 and 1")

    return signal