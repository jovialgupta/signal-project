def hdb3_decode(signal):
    """Decode AMI with HDB3 zero substitution."""
    if any(level not in (-1, 0, 1) for level in signal):
        raise ValueError("HDB3 levels must be -1, 0, or +1.")

    decoded = []
    last_polarity = -1
    index = 0

    while index < len(signal):
        current = signal[index:index + 4]

        # 000V: the violation pulse repeats the previous pulse polarity.
        if (
            len(current) == 4
            and current[:3] == [0, 0, 0]
            and current[3] == last_polarity
        ):
            decoded.extend("0000")
            last_polarity = current[3]
            index += 4
            continue

        # B00V: B alternates normally, and V repeats B's polarity.
        if (
            len(current) == 4
            and current[0] != 0
            and current[1:3] == [0, 0]
            and current[3] == current[0]
            and current[0] == -last_polarity
        ):
            decoded.extend("0000")
            last_polarity = current[3]
            index += 4
            continue

        level = signal[index]
        decoded.append("0" if level == 0 else "1")
        if level != 0:
            last_polarity = level
        index += 1

    return "".join(decoded)
