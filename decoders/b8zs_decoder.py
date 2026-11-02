def b8zs_decode(signal):
    """Decode AMI with B8ZS zero substitution."""
    if any(level not in (-1, 0, 1) for level in signal):
        raise ValueError("B8ZS levels must be -1, 0, or +1.")

    decoded = []
    last_pulse = -1
    index = 0

    # The first violation must have the same polarity as the previous pulse.
    patterns = {
        (0, 0, 0, 1, -1, 0, -1, 1): 1,
        (0, 0, 0, -1, 1, 0, 1, -1): -1,
    }

    while index < len(signal):
        current = tuple(signal[index:index + 8])
        final_polarity = patterns.get(current)

        if final_polarity is not None and current[3] == last_pulse:
            decoded.extend("00000000")
            last_pulse = final_polarity
            index += 8
            continue

        level = signal[index]
        decoded.append("0" if level == 0 else "1")
        if level != 0:
            last_pulse = level
        index += 1

    return "".join(decoded)
