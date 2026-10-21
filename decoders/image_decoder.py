from pathlib import Path

import numpy as np
from PIL import Image


def plot_waveform_for_image_decode(signal, image_path="waveform_for_decode.png"):
    """Save a clean, calibrated waveform image for pixel-based decoding."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    signal = np.asarray(signal, dtype=float)
    if signal.size == 0:
        raise ValueError("Signal cannot be empty.")
    if not np.all(np.isin(signal, [-1, 0, 1])):
        raise ValueError("Image decoder currently supports levels -1, 0, and +1.")

    fig, ax = plt.subplots(
        figsize=(max(8, len(signal) * 0.35), 3),
        dpi=150,
    )
    ax.step(
        np.arange(len(signal)),
        signal,
        where="post",
        color="black",
        linewidth=2.5,
    )
    ax.set_xlim(0, len(signal))
    # Fixed calibration makes level position interpretable from pixels alone.
    ax.set_ylim(-1.5, 1.5)
    ax.axis("off")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.05)
    fig.savefig(
        image_path,
        facecolor="white",
        bbox_inches="tight",
        pad_inches=0.08,
    )
    plt.close(fig)
    return str(image_path)



def decode_waveform_image(image_path, expected_levels):
    import numpy as np
    from PIL import Image

    if expected_levels <= 0:
        raise ValueError("expected_levels must be positive")

    image = Image.open(image_path).convert("RGB")
    pixels = np.asarray(image)
    height, width, _ = pixels.shape

    # Identify dark waveform pixels.
    dark = pixels.mean(axis=2) < 100
    recovered = []

    for i in range(expected_levels):
        # Sample the central part of this interval, avoiding transitions.
        x_start = int(i * width / expected_levels + 0.25 * width / expected_levels)
        x_end = int((i + 1) * width / expected_levels - 0.25 * width / expected_levels)
        x_end = max(x_start + 1, x_end)

        x_start = max(0, min(x_start, width - 1))
        x_end = max(x_start + 1, min(x_end, width))

        region = dark[:, x_start:x_end]

        # Find the row with the most dark waveform pixels.
        row_counts = region.sum(axis=1)
        y = int(np.argmax(row_counts))
        fraction = y / max(1, height - 1)

        if fraction < 0.35:
            recovered.append(1)
        elif fraction > 0.65:
            recovered.append(-1)
        else:
            recovered.append(0)

    return recovered
