
import numpy as np


def pcm_decode(bitstream, bits_per_sample, min_value, max_value):
    """Decode a PCM bitstream into reconstructed sample values."""

    if bits_per_sample < 1:
        raise ValueError("bits_per_sample must be at least 1")

    if any(bit not in "01" for bit in bitstream):
        raise ValueError("Bitstream must contain only 0 and 1")

    if len(bitstream) % bits_per_sample != 0:
        raise ValueError("Bitstream length must be a multiple of bits_per_sample")

    levels = 2 ** bits_per_sample

    groups = [
        bitstream[i:i + bits_per_sample]
        for i in range(0, len(bitstream), bits_per_sample)
    ]

    indices = [
        int(group, 2)
        for group in groups
    ]

    reconstructed = (
        np.array(indices, dtype=float) / (levels - 1)
    ) * (max_value - min_value) + min_value

    return reconstructed
