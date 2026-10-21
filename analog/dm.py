
import numpy as np


def dm_encode(signal, step_size=0.1):
    """Encode an analog signal using Delta Modulation."""

    signal = np.asarray(signal, dtype=float)

    if signal.size == 0:
        raise ValueError("Signal cannot be empty")

    if step_size <= 0:
        raise ValueError("Step size must be positive")

    if not np.all(np.isfinite(signal)):
        raise ValueError("Signal must contain finite numbers")

    bits = []
    reconstructed = []

    previous = signal[0]
    reconstructed.append(previous)

    for current in signal[1:]:
        if current >= previous:
            bits.append(1)
            previous += step_size
        else:
            bits.append(0)
            previous -= step_size

        reconstructed.append(previous)

    bitstream = "".join(map(str, bits))

    return bitstream, np.array(reconstructed)
