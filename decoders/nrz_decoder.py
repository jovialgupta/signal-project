def nrz_l_decode(signal):
    """Decode NRZ-L: +1 means 1, and -1 means 0."""
    levels = {1: "1", -1: "0"}
    try:
        return "".join(levels[level] for level in signal)
    except KeyError as error:
        raise ValueError("NRZ-L levels must be +1 or -1.") from error


def nrz_i_decode(signal, initial_level=-1):
    """Decode NRZ-I: a transition means 1; no transition means 0."""
    if initial_level not in (-1, 1):
        raise ValueError("Initial level must be +1 or -1.")

    if any(level not in (-1, 1) for level in signal):
        raise ValueError("NRZ-I levels must be +1 or -1.")

    bits = []
    previous_level = initial_level

    for level in signal:
        bits.append("1" if level != previous_level else "0")
        previous_level = level

    return "".join(bits)
