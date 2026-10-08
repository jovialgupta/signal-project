import numpy as np


def pcm_decode(bitstream, bits_per_sample, min_value, max_value):
    levels = 2 ** bits_per_sample
    groups = [
    bitstream[i:i + bits_per_sample]
    for i in range(0, len(bitstream), bits_per_sample)
]