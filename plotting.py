
import numpy as np
import matplotlib.pyplot as plt


def plot_digital_signal(signal, title="Digital Signal"):
    """Plot an encoded digital signal as a step waveform."""
    signal = np.asarray(signal)

    plt.figure(figsize=(10, 4))
    plt.step(
        np.arange(len(signal)),
        signal,
        where="post",
    )
    plt.title(title)
    plt.xlabel("Bit / sample position")
    plt.ylabel("Signal level")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_analog_signal(time, signal, title="Analog Signal"):
    """Plot an analog signal."""
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal, marker=".")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_comparison(original, reconstructed, title="Signal Comparison"):
    """Compare original and reconstructed signals on the same graph."""
    original = np.asarray(original)
    reconstructed = np.asarray(reconstructed)

    plt.figure(figsize=(10, 4))

    plt.plot(
        np.arange(len(original)),
        original,
        marker="o",
        label="Original",
    )

    plt.step(
        np.arange(len(reconstructed)),
        reconstructed,
        where="mid",
        label="Reconstructed",
    )

    plt.title(title)
    plt.xlabel("Sample position")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
