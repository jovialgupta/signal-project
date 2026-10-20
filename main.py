
from encoders.nrz.nrz_l import nrz_l_encode
from encoders.nrz.nrz_i import nrz_i_encode
from encoders.manchester.manchester import manchester_encode
from encoders.manchester.differential_manchester import differential_manchester_encode
from encoders.ami import ami_encode
from encoders.b8zs import b8zs_encode
from encoders.hdb3 import hdb3_encode

from decoders.nrz_decoder import nrz_l_decode, nrz_i_decode
from decoders.manchester_decoder import (
    manchester_decode,
    differential_manchester_decode,
)
from decoders.ami_decoder import ami_decode

from analog.pcm import pcm_encode, pcm_decode
from analog.dm import dm_encode, dm_decode


def plot_signal(signal, title):
    """Display a digital signal waveform."""
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(9, 4))
        plt.step(range(len(signal)), signal, where="mid")
        plt.title(title)
        plt.xlabel("Bit / sample position")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except ImportError:
        print("Matplotlib is not installed. Install it using:")
        print("python -m pip install matplotlib")


def get_bits():
    bits = input("Enter binary bits (e.g. 10110): ").strip()

    if not bits or any(bit not in "01" for bit in bits):
        print("Error: Please enter only 0 and 1.")
        return None

    return bits


def get_samples():
    raw = input("Enter sample values separated by spaces (e.g. -1 0 1): ")

    try:
        samples = [float(value) for value in raw.split()]

        if not samples:
            print("Error: Enter at least one sample.")
            return None

        return samples

    except ValueError:
        print("Error: Samples must be numbers.")
        return None


def main():
    while True:
        print("\n====================================")
        print(" DIGITAL SIGNAL ENCODER / DECODER")
        print("====================================")
        print("1. NRZ-L")
        print("2. NRZ-I")
        print("3. Manchester")
        print("4. Differential Manchester")
        print("5. AMI")
        print("6. B8ZS")
        print("7. HDB3")
        print("8. PCM")
        print("9. Delta Modulation")
        print("0. Exit")

        choice = input("Choose an option (0-9): ").strip()

        if choice == "0":
            print("Program closed. Goodbye!")
            break

        try:
            if choice in ("1", "2", "3", "4", "5", "6", "7"):
                bits = get_bits()

                if bits is None:
                    continue

                if choice == "1":
                    signal = nrz_l_encode(bits)
                    print("NRZ-L encoded:", signal)
                    print("Decoded bits:", nrz_l_decode(signal))
                    plot_signal(signal, "NRZ-L")

                elif choice == "2":
                    signal = nrz_i_encode(bits)
                    print("NRZ-I encoded:", signal)
                    print("Decoded bits:", nrz_i_decode(signal))
                    plot_signal(signal, "NRZ-I")

                elif choice == "3":
                    signal = manchester_encode(bits)
                    print("Manchester encoded:", signal)
                    print("Decoded bits:", manchester_decode(signal))
                    plot_signal(signal, "Manchester")

                elif choice == "4":
                    signal = differential_manchester_encode(bits)
                    print("Differential Manchester encoded:", signal)
                    print(
                        "Decoded bits:",
                        differential_manchester_decode(signal),
                    )
                    plot_signal(signal, "Differential Manchester")

                elif choice == "5":
                    signal = ami_encode(bits)
                    print("AMI encoded:", signal)
                    print("Decoded bits:", ami_decode(signal))
                    plot_signal(signal, "AMI")

                elif choice == "6":
                    signal = b8zs_encode(bits)
                    print("B8ZS encoded:", signal)
                    plot_signal(signal, "B8ZS")

                elif choice == "7":
                    signal = hdb3_encode(bits)
                    print("HDB3 encoded:", signal)
                    plot_signal(signal, "HDB3")

            elif choice == "8":
                samples = get_samples()

                if samples is None:
                    continue

                bits_per_sample = int(
                    input("Bits per sample (press Enter for 3): ") or "3"
                )

                bitstream, minimum, maximum = pcm_encode(
                    samples, bits_per_sample
                )
                decoded = pcm_decode(
                    bitstream, minimum, maximum, bits_per_sample
                )

                print("PCM bitstream:", bitstream)
                print("Decoded samples:", decoded)
                plot_signal(samples, "Original PCM Samples")
                plot_signal(decoded, "Reconstructed PCM Samples")

            elif choice == "9":
                samples = get_samples()

                if samples is None:
                    continue

                step_size = float(
                    input("Step size (press Enter for 0.5): ") or "0.5"
                )

                bitstream = dm_encode(samples, step_size)
                decoded = dm_decode(bitstream, step_size)

                print("Delta Modulation bits:", bitstream)
                print("Decoded samples:", decoded)
                plot_signal(samples, "Original Delta Modulation Samples")
                plot_signal(decoded, "Reconstructed Delta Modulation Samples")

            else:
                print("Invalid choice. Please enter a number from 0 to 9.")

        except (ValueError, TypeError) as error:
            print("Input or encoding error:", error)

        except Exception as error:
            print("Unexpected error:", error)


if __name__ == "__main__":
    main()
