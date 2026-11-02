from pathlib import Path
import re

import numpy as np
import matplotlib.pyplot as plt


def plot_digital_signal(signal, title="Digital Signal"):
    """Plot and save the encoded digital waveform."""
    signal = np.asarray(signal, dtype=float).ravel()

    if signal.size == 0:
        raise ValueError("Cannot plot an empty encoded signal.")

    # Extend the final level so the last bit/half-bit is visible.
    x = np.arange(signal.size + 1)
    y = np.append(signal, signal[-1])

    fig, ax = plt.subplots(figsize=(11, 4))
    ax.step(x, y, where="post", linewidth=2)
    ax.set_title(title)
    ax.set_xlabel("Bit position (half-bit position for Manchester schemes)")
    ax.set_ylabel("Signal level")
    ax.set_xticks(np.arange(signal.size + 1))
    ax.set_yticks(sorted(set(signal.tolist())))
    ax.grid(True, alpha=0.35)
    ax.set_xlim(0, signal.size)
    fig.tight_layout()

    # Save a separate image for every scheme instead of overwriting one file.
    output_dir = Path("waveforms")
    output_dir.mkdir(exist_ok=True)
    safe_title = re.sub(r"[^A-Za-z0-9_-]+", "_", title).strip("_")
    image_path = output_dir / f"{safe_title}.png"
    fig.savefig(image_path, dpi=150, bbox_inches="tight")
    print(f"Waveform image saved: {image_path.resolve()}")

    plt.show()
    plt.close(fig)


def plot_analog_signal(time, signal, title="Analog Signal"):
    """Plot an analog input signal."""
    time = np.asarray(time)
    signal = np.asarray(signal)

    if len(time) != len(signal):
        raise ValueError("Time and signal must have the same length.")

    plt.figure(figsize=(10, 4))
    plt.plot(time, signal, marker="o", linewidth=1.5)
    plt.title(title)
    plt.xlabel("Time / sample position")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_comparison(original, reconstructed, title="Signal Comparison"):
    """Compare an original signal with its reconstruction."""
    original = np.asarray(original)
    reconstructed = np.asarray(reconstructed)

    plt.figure(figsize=(10, 4))
    plt.plot(
        np.arange(len(original)),
        original,
        marker="o",
        label="Original signal",
    )
    plt.step(
        np.arange(len(reconstructed)),
        reconstructed,
        where="mid",
        label="Reconstructed signal",
    )
    plt.title(title)
    plt.xlabel("Sample position")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
