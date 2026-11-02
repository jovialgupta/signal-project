def nrz_l_encode(bits):
    """Encode 1 as +1 and 0 as -1 using NRZ-L."""
    levels = {"0": -1, "1": 1}
    try:
        return [levels[bit] for bit in bits]
    except KeyError as error:
        raise ValueError("Bits must contain only 0 and 1.") from error
