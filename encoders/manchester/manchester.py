def manchester_encode(bits):
    """Encode each bit as two half-bit levels."""
    levels = {
        "0": (-1, 1),
        "1": (1, -1),
    }
    try:
        return [level for bit in bits for level in levels[bit]]
    except KeyError as error:
        raise ValueError("Bits must contain only 0 and 1.") from error
