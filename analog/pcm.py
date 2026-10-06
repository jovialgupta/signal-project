import numpy as np


def pcm_encode(signal, bits_per_sample=3):
    signal = np.asarray(signal, dtype=float)
    samples = signal.copy()

    levels = 2 ** bits_per_sample

    min_value = np.min(samples)
    max_value = np.max(samples)

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
        