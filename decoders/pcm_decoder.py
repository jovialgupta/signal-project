import numpy as np


def pcm_decode(bitstream, bits_per_sample, min_value, max_value):
    levels = 2 ** bits_per_sample