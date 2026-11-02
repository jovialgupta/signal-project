def nrz_i_encode(bits):
    """Encode NRZ-I: a 1 causes a transition; a 0 causes no transition."""
    if any(bit not in "01" for bit in bits):
        raise ValueError("Bits must contain only 0 and 1.")

    signal = []
    current_level = -1

    for bit in bits:
        current_level *= -1 if bit == "1" else 1
        signal.append(current_level)

    return signal
