"""Regression tests for the digital signal encoder/decoder assignment."""

import itertools
import tempfile
import unittest
from pathlib import Path

import numpy as np

from analog.dm import dm_encode
from analog.pcm import pcm_encode
from data_generator import (
    generate_bits_with_zero_run,
    longest_palindrome,
    longest_palindromic_subsequence,
)
from decoders.ami_decoder import ami_decode
from decoders.b8zs_decoder import b8zs_decode
from decoders.delta_decoder import dm_decode
from decoders.hdb3_decoder import hdb3_decode
from decoders.image_decoder import (
    decode_waveform_image,
    plot_waveform_for_image_decode,
)
from decoders.manchester_decoder import (
    differential_manchester_decode,
    manchester_decode,
)
from decoders.nrz_decoder import nrz_i_decode, nrz_l_decode
from decoders.pcm_decoder import pcm_decode
from encoders.ami import ami_encode
from encoders.b8zs import b8zs_encode
from encoders.hdb3 import hdb3_encode
from encoders.manchester.differential_manchester import (
    differential_manchester_encode,
)
from encoders.manchester.manchester import manchester_encode
from encoders.nrz.nrz_i import nrz_i_encode
from encoders.nrz.nrz_l import nrz_l_encode


class LineCodingRoundTripTests(unittest.TestCase):
    def test_all_line_codes_round_trip(self):
        schemes = (
            (nrz_l_encode, nrz_l_decode),
            (nrz_i_encode, nrz_i_decode),
            (manchester_encode, manchester_decode),
            (
                differential_manchester_encode,
                differential_manchester_decode,
            ),
            (ami_encode, ami_decode),
            (b8zs_encode, b8zs_decode),
            (hdb3_encode, hdb3_decode),
        )

        for length in range(1, 9):
            for values in itertools.product("01", repeat=length):
                bits = "".join(values)
                for encoder, decoder in schemes:
                    with self.subTest(bits=bits, encoder=encoder.__name__):
                        self.assertEqual(decoder(encoder(bits)), bits)

    def test_encoders_reject_non_binary_input(self):
        encoders = (
            nrz_l_encode,
            nrz_i_encode,
            manchester_encode,
            differential_manchester_encode,
            ami_encode,
            b8zs_encode,
            hdb3_encode,
        )
        for encoder in encoders:
            with self.subTest(encoder=encoder.__name__):
                with self.assertRaises(ValueError):
                    encoder("0102")


class ImageDecoderTests(unittest.TestCase):
    def test_image_decoder_recovers_levels_from_pixels(self):
        signals = (
            [1, -1, 0, 1, 0, -1],
            [0, 0, 0, -1, 1, 0, 1, -1],
            [1, -1] * 10,
        )
        with tempfile.TemporaryDirectory() as directory:
            for index, signal in enumerate(signals):
                image_path = Path(directory) / f"waveform_{index}.png"
                plot_waveform_for_image_decode(signal, str(image_path))
                recovered = decode_waveform_image(
                    str(image_path),
                    expected_levels=len(signal),
                )
                self.assertEqual(recovered, signal)


class AnalogModulationTests(unittest.TestCase):
    def test_pcm_encoder_decoder(self):
        samples = np.array([-1.0, -0.2, 0.4, 1.0])
        bits, minimum, maximum = pcm_encode(samples, bits_per_sample=3)
        reconstructed = pcm_decode(bits, 3, minimum, maximum)
        self.assertEqual(len(bits), len(samples) * 3)
        self.assertEqual(len(reconstructed), len(samples))
        self.assertTrue(np.all(np.isfinite(reconstructed)))

    def test_pcm_constant_signal(self):
        samples = np.array([2.5, 2.5, 2.5])
        bits, minimum, maximum = pcm_encode(samples, bits_per_sample=3)
        reconstructed = pcm_decode(bits, 3, minimum, maximum)
        np.testing.assert_allclose(reconstructed, samples)

    def test_delta_modulation_staircase_round_trip(self):
        samples = np.array([0.0, 0.3, 0.1, 0.8, 0.6])
        bits, encoder_staircase = dm_encode(samples, step_size=0.1)
        decoder_staircase = dm_decode(
            bits,
            step_size=0.1,
            initial_value=float(samples[0]),
        )
        np.testing.assert_allclose(decoder_staircase, encoder_staircase)


class DataGeneratorTests(unittest.TestCase):
    def test_zero_run_generator_contains_requested_run(self):
        for zero_count in (4, 8):
            bits = generate_bits_with_zero_run(24, zero_count)
            self.assertEqual(len(bits), 24)
            self.assertIn("0" * zero_count, bits)

    def test_longest_palindromic_subsequence(self):
        self.assertEqual(longest_palindrome("01010"), "01010")
        self.assertEqual(longest_palindrome("100101"), "010")
        subsequence = longest_palindromic_subsequence("100101")
        self.assertEqual(subsequence, "10101")
        self.assertEqual(subsequence, subsequence[::-1])


if __name__ == "__main__":
    unittest.main()
