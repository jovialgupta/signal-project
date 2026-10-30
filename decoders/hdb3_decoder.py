
def hdb3_decode(signal):
    decoded = []
    i = 0

    # Must match the initial polarity in your HDB3 encoder
    last_polarity = -1

    while i < len(signal):

        if i + 4 <= len(signal):
            current = signal[i:i + 4]

            # Check for 000V pattern
            if (
                current[0:3] == [0, 0, 0]
                and current[3] == last_polarity
            ):
                decoded.extend("0000")
                last_polarity = current[3]
                i += 4
                continue

            # Check for B00V pattern
            if (
                current[0] != 0
                and current[1:3] == [0, 0]
                and current[3] == current[0]
                and current[0] == -last_polarity
            ):
                decoded.extend("0000")
                last_polarity = current[3]
                i += 4
                continue

        # Normal AMI decoding
        if signal[i] == 0:
            decoded.append("0")
        else:
            decoded.append("1")
            last_polarity = signal[i]

        i += 1

    return "".join(decoded)
