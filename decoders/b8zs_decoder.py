
def b8zs_decode(signal):
    decoded = []
    i = 0

    # The two possible B8ZS substitution patterns
    patterns = [
        [0, 0, 0, 1, -1, 0, -1, 1],
        [0, 0, 0, -1, 1, 0, 1, -1]
    ]

    while i < len(signal):

        # Check whether 8 values are available
        if i + 8 <= len(signal):

            current = signal[i:i + 8]

            # Check if the current 8 values match a B8ZS pattern
            if current in patterns:

                # Replace the special pattern with 8 zeros
                decoded.extend("00000000")

                # Skip the 8 values already decoded
                i += 8
                continue

        # Normal AMI decoding
        if signal[i] == 0:
            decoded.append("0")
        else:
            decoded.append("1")

        i += 1

    return "".join(decoded)
