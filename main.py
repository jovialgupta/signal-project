import numpy as np
from decoders.image_decoder import decode_waveform_image
from decoders.image_decoder import plot_waveform_for_image_decode

from data_generator import generate_data, longest_palindrome

from encoders.nrz.nrz_l import nrz_l_encode
from encoders.nrz.nrz_i import nrz_i_encode
from encoders.manchester.manchester import manchester_encode
from encoders.manchester.differential_manchester import (
    differential_manchester_encode,
)
from encoders.ami import ami_encode
from encoders.b8zs import b8zs_encode
from encoders.hdb3 import hdb3_encode

from decoders.nrz_decoder import nrz_l_decode, nrz_i_decode
from decoders.manchester_decoder import (
    manchester_decode,
    differential_manchester_decode,
)
from decoders.ami_decoder import ami_decode
from decoders.pcm_decoder import pcm_decode
from decoders.delta_decoder import dm_decode

from analog.pcm import pcm_encode
from analog.dm import dm_encode

from plotting import (
    plot_digital_signal,
    plot_analog_signal,
    plot_comparison,
)


def get_choice(prompt, valid_choices):
    """Keep asking until the user enters a valid choice."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Try again.")


def get_integer(prompt, default, minimum=1):
    while True:
        raw = input(f"{prompt} (default {default}): ").strip()
        try:
            value = int(raw) if raw else default
            if value >= minimum:
                return value
            print(f"Enter a value >= {minimum}.")
        except ValueError:
            print("Enter a valid integer.")


def get_float(prompt, default):
    while True:
        raw = input(f"{prompt} (default {default}): ").strip()
        try:
            value = float(raw) if raw else default
            if np.isfinite(value):
                return value
            print("Enter a finite number.")
        except ValueError:
            print("Enter a valid number.")


def get_bits():
    while True:
        bits = input("Enter binary bits: ").strip()
        if bits and all(bit in "01" for bit in bits):
            return bits
        print("Enter a non-empty sequence containing only 0 and 1.")


def get_samples():
    while True:
        raw = input(
            "Enter sample values separated by spaces "
            "(e.g. -1 0 0.5 1): "
        ).strip()
        try:
            samples = np.array(
                [float(value) for value in raw.split()],
                dtype=float,
            )
            if samples.size and np.all(np.isfinite(samples)):
                return samples
            print("Enter at least one finite numerical sample.")
        except ValueError:
            print("Samples must be numbers.")


def choose_digital_data():
    print("\n--- Digital Data Generator ---")
    print("1. Generate random bits")
    print("2. Generate bits containing 4 consecutive zeros")
    print("3. Generate bits containing 8 consecutive zeros")
    print("4. Enter bits manually")

    choice = get_choice("Choose (1-4): ", {"1", "2", "3", "4"})

    if choice == "4":
        bits = get_bits()
    else:
        length = get_integer("Sequence length", 16)

        if choice == "1":
            bits, _ = generate_data("random", length)
        else:
            zero_count = 4 if choice == "2" else 8

            if length < zero_count:
                print(
                    f"Length must be at least {zero_count}. "
                    "Using manual input instead."
                )
                bits = get_bits()
            else:
                bits, _ = generate_data("zeros", length, zero_count)

    palindrome = longest_palindrome(bits)
    print("\nGenerated digital data:", bits)
    print("Longest palindrome:", palindrome)
    print("Palindrome length:", len(palindrome))
    return bits


def choose_line_encoder():
    print("\n--- Line Coding ---")
    print("1. NRZ-L")
    print("2. NRZ-I")
    print("3. Manchester")
    print("4. Differential Manchester")
    print("5. AMI")
    print("6. B8ZS")
    print("7. HDB3")

    choice = get_choice("Choose encoder (1-7): ", set("1234567"))

    encoders = {
        "1": ("NRZ-L", nrz_l_encode, nrz_l_decode),
        "2": ("NRZ-I", nrz_i_encode, nrz_i_decode),
        "3": ("Manchester", manchester_encode, manchester_decode),
        "4": (
            "Differential Manchester",
            differential_manchester_encode,
            differential_manchester_decode,
        ),
        "5": ("AMI", ami_encode, ami_decode),
        "6": ("B8ZS", b8zs_encode, None),
        "7": ("HDB3", hdb3_encode, None),
    }

    return encoders[choice]


def run_line_coding(bits):
    name = get_choice(
        "Choose line encoding (nrz_l/nrz_i/manchester/diff_manchester/ami/b8zs/hdb3): ",
        {
            "nrz_l",
            "nrz_i",
            "manchester",
            "diff_manchester",
            "ami",
            "b8zs",
            "hdb3",
        },
    )

    # Select the encoder and its matching decoder
    encoders = {
        "nrz_l": (nrz_l_encode, nrz_l_decode),
        "nrz_i": (nrz_i_encode, nrz_i_decode),
        "manchester": (manchester_encode, manchester_decode),
        "diff_manchester": (
            differential_manchester_encode,
            differential_manchester_decode,
        ),
        "ami": (ami_encode, ami_decode),
        "b8zs": (b8zs_encode, None),
        "hdb3": (hdb3_encode, None),
    }

    encoder, decoder = encoders[name]

    # Encode the original bit sequence
    encoded = encoder(bits)

    print("\nOriginal bits:", bits)
    print("Encoded signal:", encoded)

    # Ask whether to decode the waveform image
    decode = get_choice(
        "Decode the signal from its waveform image? (y/n): ",
        {"y", "n"},
    )

    if decode == "n":
        return

    if decoder is None:
        print(f"No decoder is available for {name}.")
        return

    try:
        image_path = plot_waveform_for_image_decode(
            encoded,
            "waveform_for_decode.png",
        )
        print("Waveform image saved:", image_path)

        recovered_signal = decode_waveform_image(
            image_path,
            expected_levels=len(encoded),
        )

        decoded = decoder(recovered_signal)

        print("Signal recovered from image:", recovered_signal)
        print("Decoded bits:", decoded)
        print("Original bits:", bits)
        print("Match:", decoded == bits)

    except (ValueError, TypeError, OSError) as error:
        print("Image decoding error:", error)




def run_pcm():
    print("\n--- Pulse Code Modulation (PCM) ---")
    samples = get_samples()
    bits_per_sample = get_integer("Bits per sample", 3)

    bitstream, minimum, maximum = pcm_encode(
        samples,
        bits_per_sample=bits_per_sample,
    )

    print("\nPCM bitstream:", bitstream)
    plot_analog_signal(
        np.arange(len(samples)),
        samples,
        "Original PCM Samples",
    )

    decode = get_choice("Decode the PCM bitstream? (y/n): ", {"y", "n"})

    if decode == "y":
        reconstructed = pcm_decode(
            bitstream,
            bits_per_sample,
            minimum,
            maximum,
        )
        print("Reconstructed PCM samples:", reconstructed)
        plot_comparison(
            samples,
            reconstructed,
            "Original vs Reconstructed PCM",
        )

    if get_choice(
        "Pass PCM bits to line coding? (y/n): ",
        {"y", "n"},
    ) == "y":
        run_line_coding(bitstream)


def run_dm():
    print("\n--- Delta Modulation (DM) ---")
    samples = get_samples()
    step_size = get_float("Step size", 0.1)

    if step_size <= 0:
        print("Step size must be positive.")
        return

    bitstream, encoder_staircase = dm_encode(
        samples,
        step_size=step_size,
    )

    print("\nDelta Modulation bitstream:", bitstream)
    print("Encoder staircase:", encoder_staircase)
    plot_comparison(
        samples,
        encoder_staircase,
        "Original Signal vs DM Encoder Staircase",
    )

    decode = get_choice("Decode the DM bitstream? (y/n): ", {"y", "n"})

    if decode == "y":
        reconstructed = dm_decode(
            bitstream,
            step_size=step_size,
            initial_value=float(samples[0]),
        )
        print("Decoded staircase:", reconstructed)
        plot_comparison(
            encoder_staircase,
            reconstructed,
            "Encoder Staircase vs Decoded Staircase",
        )

    if bitstream and get_choice(
        "Pass DM bits to line coding? (y/n): ",
        {"y", "n"},
    ) == "y":
        run_line_coding(bitstream)
    elif not bitstream:
        print("No DM bits were generated; skipping line coding.")


def main():
    while True:
        print("\n======================================")
        print(" DIGITAL SIGNAL ENCODER / DECODER")
        print("======================================")
        print("1. Digital input and line coding")
        print("2. Analog input and PCM")
        print("3. Analog input and Delta Modulation")
        print("0. Exit")

        choice = get_choice(
            "Choose an option (0-3): ",
            {"0", "1", "2", "3"},
        )

        if choice == "0":
            print("Program closed. Goodbye!")
            break

        try:
            if choice == "1":
                bits = choose_digital_data()
                run_line_coding(bits)
            elif choice == "2":
                run_pcm()
            elif choice == "3":
                run_dm()
        except (ValueError, TypeError, IndexError) as error:
            print("\nInput or processing error:", error)
        except Exception as error:
            print("\nUnexpected error:", error)


if __name__ == "__main__":
    main()
