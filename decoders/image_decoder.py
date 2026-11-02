"""OpenCV-based decoding of a calibrated digital waveform image.

Only the saved image is read by the decoder. The original encoded signal
values are never supplied to this module.
"""

import cv2
import numpy as np


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

    # One equal-width horizontal cell represents each encoded signal level.
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
    """Recover signal levels from waveform pixels using OpenCV.

    expected_levels is the number of equal-width signal cells in the plotted
    image. It is framing information only; no encoded values are provided.
    """
    if not isinstance(expected_levels, int) or expected_levels <= 0:
        raise ValueError("expected_levels must be a positive integer.")

    grayscale = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if grayscale is None:
        raise ValueError(f"Could not read waveform image: {image_path}")

    height, width = grayscale.shape
    if width < expected_levels:
        raise ValueError("Image is too narrow for the requested signal cells.")

    # Otsu thresholding separates the dark waveform from the light background.
    _, waveform_mask = cv2.threshold(
        grayscale,
        0,
        255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU,
    )

    recovered = []
    for index in range(expected_levels):
        center_x = int((index + 0.5) * width / expected_levels)
        # A small horizontal window makes sampling less sensitive to
        # antialiasing or a one-pixel alignment difference.
        half_window = max(1, width // (expected_levels * 100))
        left = max(0, center_x - half_window)
        right = min(width, center_x + half_window + 1)

        dark_rows = np.where(waveform_mask[:, left:right] > 0)[0]
        if dark_rows.size == 0:
            raise ValueError(
                f"No waveform pixels found in signal cell {index}."
            )

        # The median row is robust to the waveform's line thickness.
        normalized_y = float(np.median(dark_rows)) / max(1, height - 1)

        # The plot is calibrated: +1 is in the upper third, 0 in the
        # middle third, and -1 in the lower third of the image.
        if normalized_y < 1 / 3:
            recovered.append(1)
        elif normalized_y > 2 / 3:
            recovered.append(-1)
        else:
            recovered.append(0)

    return recovered
