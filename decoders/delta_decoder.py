
import numpy as np


def dm_decode(bitstream, step_size=0.1, initial_value=0.0):
    """Decode a Delta Modulation bitstream into a staircase signal."""

    if step_size <= 0:
        raise ValueError("Step size must be positive")

    if any(bit not in "01" for bit in bitstream):
        raise ValueError("Bitstream must contain only 0 and 1")

    current = initial_value
    staircase = [current]

    for bit in bitstream:
        if bit == "1":
            current += step_size
        else:
            current -= step_size

        staircase.append(current)

    return np.array(staircase)
