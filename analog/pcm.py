import numpy as np


def sample_signal(signal, sample_rate):
    # Sampling
    pass


def quantize_signal(samples, levels):
    # Quantization
    pass


def pcm_encode(signal, sample_rate, bits_per_sample):
    # Sampling
    # Quantization
    # Binary encoding
    pass


def pcm_decode(bitstream, bits_per_sample, min_value, max_value):
    # Binary → quantized values
    # Reconstruct approximate analog signal
    pass