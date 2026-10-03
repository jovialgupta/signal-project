import numpy as np


def pcm_encode(signal, bits_per_sample=3):
    signal = np.asarray(signal, dtype=float)
    samples = signal.copy()

    levels = 2 ** bits_per_sample