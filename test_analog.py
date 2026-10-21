
import numpy as np

from analog.pcm import pcm_encode
from decoders.pcm_decoder import pcm_decode
from analog.dm import dm_encode
from decoders.delta_decoder import dm_decode


def test_pcm():
    samples = np.array([-1.0, 0.0, 1.0])

    bits, minimum, maximum = pcm_encode(
        samples,
        bits_per_sample=3,
    )

    reconstructed = pcm_decode(
        bits,
        3,
        minimum,
        maximum,
    )

    print("\n--- PCM ---")
    print("Original samples:", samples)
    print("Encoded bits:", bits)
    print("Reconstructed samples:", reconstructed)

    assert len(bits) == len(samples) * 3
    assert len(reconstructed) == len(samples)
    assert np.all(np.isfinite(reconstructed))
    print("PASS: PCM encoding and decoding")


def test_dm():
    samples = np.array([0.0, 0.2, 0.5, 0.1])
    step_size = 0.1

    bits, encoder_staircase = dm_encode(
        samples,
        step_size=step_size,
    )

    decoded = dm_decode(
        bits,
        step_size=step_size,
        initial_value=float(samples[0]),
    )

    print("\n--- Delta Modulation ---")
    print("Original samples:", samples)
    print("Encoded bits:", bits)
    print("Encoder staircase:", encoder_staircase)
    print("Decoder staircase:", decoded)

    assert len(bits) == len(samples) - 1
    assert np.allclose(encoder_staircase, decoded)
    print("PASS: DM encoder and decoder staircases match")


if __name__ == "__main__":
    test_pcm()
    test_dm()
