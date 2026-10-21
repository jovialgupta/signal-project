
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
    if max_value == min_value:
        quantized_values = np.full(len(samples), min_value)
    else:
        quantized_values = (
            indices / (levels - 1)
        ) * (max_value - min_value) + min_value

    return samples, quantized_values
        
