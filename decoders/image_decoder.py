"""Pixel-based decoding of a calibrated digital waveform image.

The decoder reads pixel positions from the saved PNG. It does not receive
or inspect the original encoded signal values.
"""

import numpy as np
from PIL import Image


def plot_waveform_for_image_decode(signal, image_path="waveform_for_decode.png"):
    """Save a calibrated waveform image with equal-width signal cells."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    signal = np.asarray(signal, dtype=float)
    if signal.size == 0:
        raise ValueError("Signal cannot be empty.")
    if not np.all(np.isin(signal, [-1, 0, 1])):
        raise ValueError("Image decoder supports levels -1, 0, and +1.")

    # Use one equal-width cell per encoded level and remove all plot margins.
    figure = plt.figure(
        figsize=(max(8, len(signal) * 0.35), 3),
        dpi=150,
    )
    axis = figure.add_axes([0, 0, 1, 1])
    extended_signal = np.append(signal, signal[-1])
    axis.step(
        np.arange(len(extended_signal)),
        extended_signal,
        where="post",
        color="black",
        linewidth=2.5,
    )
    axis.set_xlim(0, len(signal))
    axis.set_ylim(-1.5, 1.5)
    axis.axis("off")
    figure.savefig(image_path, facecolor="white", pad_inches=0)
    plt.close(figure)
    return str(image_path)


def decode_waveform_image(image_path, expected_levels):
    """Recover -1, 0, +1 levels by examining waveform pixels in a PNG."""
    if expected_levels <= 0:
        raise ValueError("expected_levels must be positive.")

    image = Image.open(image_path).convert("RGB")
    pixels = np.asarray(image)
    height, width, _ = pixels.shape
    dark_pixels = pixels.mean(axis=2) < 100

    recovered = []
    for index in range(expected_levels):
        # Sample the center of each bit/half-bit cell, away from transitions.
        x_position = min(
            width - 1,
            int((index + 0.5) * width / expected_levels),
        )
        dark_rows = np.flatnonzero(dark_pixels[:, x_position])

        if dark_rows.size == 0:
            raise ValueError(
                f"No waveform pixel found in signal cell {index}."
            )

        # Select the dark row closest to the calibrated zero-level center.
        center_row = (height - 1) / 2
        y_position = dark_rows[
            np.argmin(np.abs(dark_rows - center_row))
        ]
        normalized_y = y_position / max(1, height - 1)

        # With image y increasing downwards: +1 is upper, -1 is lower.
        if normalized_y < 0.42:
            recovered.append(1)
        elif normalized_y > 0.58:
            recovered.append(-1)
        else:
            recovered.append(0)

    return recovered
