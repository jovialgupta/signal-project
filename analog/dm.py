
import numpy as np


def dm_encode(signal, step_size=0.5, initial_value=0.0):
    """Encode samples using basic delta modulation."""
    samples = np.asarray(signal, dtype=float)

    if samples.size == 0:
        raise ValueError("Signal cannot be empty")
    if step_size <= 0:
        raise ValueError("step_size must be positive")
    if not np.all(np.isfinite(samples)):
        raise ValueError("Signal must contain finite numbers")

    bits = []
    reconstructed = float(initial_value)

    for sample in samples:
        if sample >= reconstructed:
            bits.append("1")
            reconstructed += step_size
        else:
            bits.append("0")
            reconstructed -= step_size

    return "".join(bits)


def dm_decode(bitstream, step_size=0.5, initial_value=0.0):
    """Reconstruct an approximate signal from delta modulation bits."""
    if step_size <= 0:
        raise ValueError("step_size must be positive")
    if any(bit not in "01" for bit in bitstream):
        raise ValueError("Bitstream must contain only 0 and 1")

    reconstructed = float(initial_value)
    samples = []

    for bit in bitstream:
        if bit == "1":
            reconstructed += step_size
        else:
            reconstructed -= step_size

        samples.append(reconstructed)

    return np.asarray(samples)
