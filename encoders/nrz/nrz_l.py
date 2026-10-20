def nrz_l_encode(bits):
    signal = []

    for bit in bits:
        if bit == '1':
            signal.append(1)
        else:
            signal.append(-1)

    return signal