
import numpy as np


def pcm_encode(signal, bits_per_sample=3):
    """Quantize samples and encode them as a binary bitstream."""
    samples = np.asarray(signal, dtype=float)

    if samples.size == 0:
        raise ValueError("Signal cannot be empty")
    if bits_per_sample < 1:
        raise ValueError("bits_per_sample must be at least 1")
    if not np.all(np.isfinite(samples)):
        raise ValueError("Signal must contain finite numbers")

    levels = 2 ** bits_per_sample
    min_value = float(np.min(samples))
    max_value = float(np.max(samples))

    if max_value == min_value:
        indices = np.zeros(len(samples), dtype=int)
    else:
        normalized = (samples - min_value) / (max_value - min_value)
        indices = np.round(normalized * (levels - 1)).astype(int)

    bitstream = "".join(
        format(int(index), f"0{bits_per_sample}b")
        for index in indices
    )

    # Keep the range so the decoder can reconstruct approximate samples.
    return bitstream, min_value, max_value


def pcm_decode(bitstream, min_value, max_value, bits_per_sample=3):
    """Decode a PCM bitstream into approximate sample values."""
    if bits_per_sample < 1:
        raise ValueError("bits_per_sample must be at least 1")
    if len(bitstream) % bits_per_sample != 0:
        raise ValueError("Bitstream length must be divisible by bits_per_sample")
    if any(bit not in "01" for bit in bitstream):
        raise ValueError("Bitstream must contain only 0 and 1")
    if max_value < min_value:
        raise ValueError("max_value must be >= min_value")

    levels = 2 ** bits_per_sample
    samples = []

    for i in range(0, len(bitstream), bits_per_sample):
        index = int(bitstream[i:i + bits_per_sample], 2)

        if min_value == max_value:
            sample = min_value
        else:
            sample = min_value + (
                index / (levels - 1)
            ) * (max_value - min_value)

        samples.append(sample)

    return np.asarray(samples)
