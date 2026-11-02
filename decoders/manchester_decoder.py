def manchester_decode(signal):
    """Decode Manchester pairs: (+1, -1) is 1 and (-1, +1) is 0."""
    if len(signal) % 2:
        raise ValueError("Manchester signal must contain an even number of levels.")

    pairs = {
        (1, -1): "1",
        (-1, 1): "0",
    }
    bits = []

    for index in range(0, len(signal), 2):
        pair = (signal[index], signal[index + 1])
        try:
            bits.append(pairs[pair])
        except KeyError as error:
            raise ValueError("Invalid Manchester signal pair.") from error

    return "".join(bits)


def differential_manchester_decode(signal, initial_level=-1):
    """Decode Differential Manchester using initial level -1 by default."""
    if len(signal) % 2:
        raise ValueError("Signal must contain an even number of levels.")

    if initial_level not in (-1, 1):
        raise ValueError("Initial level must be +1 or -1.")

    if any(level not in (-1, 1) for level in signal):
        raise ValueError("Signal levels must be +1 or -1.")

    bits = []
    previous_level = initial_level

    for index in range(0, len(signal), 2):
        first_half, second_half = signal[index:index + 2]

        if second_half != -first_half:
            raise ValueError("Missing Differential Manchester mid-bit transition.")

        bits.append("1" if first_half == previous_level else "0")
        previous_level = second_half

    return "".join(bits)
