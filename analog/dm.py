import numpy as np


def delta_encode(signal, step_size=0.1):
    signal = np.asarray(signal, dtype=float)

    bits = []
    reconstructed = []

    previous = signal[0]

    reconstructed.append(previous)
    for current in signal[1:]:
        if current >= previous:
            bits.append(1)
            previous = previous + step_size
        else:
            bits.append(0)
            previous = previous - step_size
            reconstructed.append(previous)
            return bits, np.array(reconstructed)