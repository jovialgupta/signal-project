
import numpy as np
from plotting import plot_comparison

original = [0.0, 0.2, 0.5, 0.1]
reconstructed = [0.0, 0.1, 0.2, 0.1]

plot_comparison(
    original,
    reconstructed,
    "Test: Original vs Reconstructed",
)
