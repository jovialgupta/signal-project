
def nrz_l_decode(signal):
    """Decode NRZ-L: +1 means 1, and -1 means 0."""
    bits = ""

    for level in signal:
        if level == 1:
            bits += "1"
        elif level == -1:
            bits += "0"
        else:
            raise ValueError("NRZ-L levels must be +1 or -1")

    return bits


def nrz_i_decode(signal, initial_level=-1):
    """Decode NRZ-I: a transition means 1; no transition means 0."""
    bits = ""
    previous_level = initial_level

    for level in signal:
        if level not in (-1, 1):
            raise ValueError("NRZ-I levels must be +1 or -1")

        bits += "1" if level != previous_level else "0"
        previous_level = level

    return bits
