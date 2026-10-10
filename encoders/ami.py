def ami_encode(bits):
    signal = []
    last_level = -1

    for bit in bits:
        if bit == '0':
            signal.append(0)
        elif bit == '1':
            last_level *= -1
            signal.append(last_level)
        else:
            raise ValueError("Bits must contain only 0 and 1")

    return signal