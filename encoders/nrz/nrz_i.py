def nrz_i_encode(bits):
    signal = []
    current_level = -1

    for bit in bits:
        if bit == '1':
            current_level *= -1

        signal.append(current_level)

    return signal