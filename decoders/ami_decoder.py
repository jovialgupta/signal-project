
def ami_decode(signal):
    """Decode AMI: zero levels mean 0; positive or negative pulses mean 1."""
    if any(level not in (-1, 0, 1) for level in signal):
        raise ValueError("AMI levels must be -1, 0, or +1")

    return "".join("0" if level == 0 else "1" for level in signal)
