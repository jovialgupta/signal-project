
def b8zs_encode(bits):
    if any(bit not in '01' for bit in bits):
        raise ValueError("Bits must contain only 0 and 1")

    signal = []
    last_level = -1
    i = 0

    while i < len(bits):
        # Replace eight consecutive zeros
        if bits[i:i + 8] == '00000000':
            if last_level == 1:
                pattern = [0, 0, 0, 1, -1, 0, -1, 1]
            else:
                pattern = [0, 0, 0, -1, 1, 0, 1, -1]

            signal.extend(pattern)
            last_level = pattern[-1]
            i += 8

        elif bits[i] == '0':
            signal.append(0)
            i += 1

        else:
            last_level *= -1
            signal.append(last_level)
            i += 1

    return signal
