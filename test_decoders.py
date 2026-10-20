
from encoders.nrz.nrz_l import nrz_l_encode
from encoders.nrz.nrz_i import nrz_i_encode
from encoders.manchester.manchester import manchester_encode
from encoders.manchester.differential_manchester import (
    differential_manchester_encode,
)
from encoders.ami import ami_encode

from decoders.nrz_decoder import nrz_l_decode, nrz_i_decode
from decoders.manchester_decoder import (
    manchester_decode,
    differential_manchester_decode,
)
from decoders.ami_decoder import ami_decode


TEST_BITS = [
    "10110",
    "0000",
    "1111",
    "10101010",
    "100000001",
]


def run_test(name, encoder, decoder, bits):
    try:
        encoded = encoder(bits)
        decoded = decoder(encoded)

        if decoded == bits:
            print(f"PASS: {name} | {bits} -> {decoded}")
        else:
            print(
                f"FAIL: {name} | expected {bits}, "
                f"got {decoded}; encoded={encoded}"
            )
    except Exception as error:
        print(f"ERROR: {name} | {bits} | {error}")


def main():
    tests = [
        ("NRZ-L", nrz_l_encode, nrz_l_decode),
        ("NRZ-I", nrz_i_encode, nrz_i_decode),
        ("Manchester", manchester_encode, manchester_decode),
        (
            "Differential Manchester",
            differential_manchester_encode,
            differential_manchester_decode,
        ),
        ("AMI", ami_encode, ami_decode),
    ]

    for name, encoder, decoder in tests:
        print(f"\n--- {name} ---")
        for bits in TEST_BITS:
            run_test(name, encoder, decoder, bits)


if __name__ == "__main__":
    main()
