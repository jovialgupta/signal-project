
import numpy as np
import matplotlib.pyplot as plt


def plot_digital_signal(signal, title="Digital Signal"):
    """Plot encoded digital signal levels."""
    signal = np.asarray(signal)

    plt.figure(figsize=(10, 4))
    plt.step(
        np.arange(len(signal)),
        signal,
        where="post",
        linewidth=1.8,
    )
    plt.title(title)
    plt.xlabel("Bit / sample position")
    plt.ylabel("Signal level")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


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
