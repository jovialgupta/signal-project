
def manchester_decode(signal):
    """Decode Manchester pairs: [1,-1] means 1; [-1,1] means 0."""
    if len(signal) % 2 != 0:
        raise ValueError("Manchester signal must contain an even number of levels")

    bits = ""

    for i in range(0, len(signal), 2):
        pair = signal[i:i + 2]

        if pair == [1, -1]:
            bits += "1"
        elif pair == [-1, 1]:
            bits += "0"
        else:
            raise ValueError("Invalid Manchester signal pair")

    return bits


def differential_manchester_decode(signal, initial_level=-1):
    """Decode Differential Manchester using initial level -1 by default."""
    if len(signal) % 2 != 0:
        raise ValueError("Signal must contain an even number of levels")

    if initial_level not in (-1, 1):
        raise ValueError("Initial level must be +1 or -1")

    bits = ""
    previous_level = initial_level

    for i in range(0, len(signal), 2):
        first_half = signal[i]
        second_half = signal[i + 1]

        if first_half not in (-1, 1) or second_half not in (-1, 1):
            raise ValueError("Signal levels must be +1 or -1")

        if first_half == previous_level:
            bits += "1"
        else:
            bits += "0"

        if second_half != -first_half:
            raise ValueError("Invalid Differential Manchester mid-bit transition")

        previous_level = second_half

    return bits
