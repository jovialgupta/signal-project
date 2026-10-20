
def differential_manchester_encode(bits):
    signal = []
    current_level = -1

    for bit in bits:
        if bit not in '01':
            raise ValueError("Bits must contain only 0 and 1")

        # A 0 causes a transition at the beginning of the bit
        if bit == '0':
            current_level *= -1

        # First half of the bit
        signal.append(current_level)

        # Always transition in the middle of the bit
        current_level *= -1
        signal.append(current_level)

    return signal