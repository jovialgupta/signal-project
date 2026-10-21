
def hdb3_encode(bits):
    """Encode binary data using AMI with HDB3 zero substitution."""
    if any(bit not in "01" for bit in bits):
        raise ValueError("Bits must contain only 0 and 1")

    signal = []
    last_level = -1
    pulse_count = 0
    i = 0

    while i < len(bits):
        if bits[i:i + 4] == "0000":
            if pulse_count % 2 == 1:
                # Odd number of normal pulses: 000V
                # V has the same polarity as the preceding pulse.
                violation = last_level
                signal.extend([0, 0, 0, violation])
                last_level = violation
            else:
                # Even number of normal pulses: B00V
                # B alternates normally; V violates AMI polarity.
                balancing = -last_level
                violation = balancing
                signal.extend([balancing, 0, 0, violation])
                last_level = violation

            pulse_count = 0
            i += 4

        elif bits[i] == "0":
            signal.append(0)
            i += 1

        else:
            last_level *= -1
            signal.append(last_level)
            pulse_count += 1
            i += 1

    return signal
