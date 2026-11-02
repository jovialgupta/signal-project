# Digital Signal Encoder and Decoder

## Project overview
A Python implementation of digital data generation, line coding, AMI scrambling, PCM, Delta Modulation, and waveform-based decoding.

## Features
- Generate random binary data, data containing four or eight consecutive zeros, or enter a binary stream manually.
- Find the longest contiguous palindromic substring with Manacher's algorithm (O(n)); also report the longest palindromic subsequence (O(n²)) to cover the alternate interpretation of the assignment wording.
- Line coding: NRZ-L, NRZ-I, Manchester, Differential Manchester, and AMI.
- AMI options: no scrambling, B8ZS, or HDB3.
- Analog input: PCM or Delta Modulation, including corresponding decoding. The DM decoder produces the reconstructed staircase.
- Optionally pass PCM/DM output bits to a line-coding scheme.
- Extra credit: decode the selected line code from a saved waveform PNG by examining image pixels rather than reading the original encoded values.
- Automated regression tests for line-code round trips, image decoding, PCM, DM, and palindrome output.

## Requirements
Python 3 and the packages listed in requirements.txt:
- NumPy
- Matplotlib
- Pillow

Install dependencies:

~~~bash
python -m pip install -r requirements.txt
~~~

## Run

~~~bash
python main.py
~~~

## Run tests

~~~bash
python -m unittest discover -s tests
~~~

## Project structure

~~~text
signal-project/
├── main.py
├── data_generator.py
├── plotting.py
├── requirements.txt
├── SPECIFICATION.md
├── encoders/
│   ├── nrz/
│   ├── manchester/
│   ├── ami.py
│   ├── b8zs.py
│   └── hdb3.py
├── decoders/
│   ├── image_decoder.py
│   ├── nrz_decoder.py
│   ├── manchester_decoder.py
│   ├── ami_decoder.py
│   ├── b8zs_decoder.py
│   ├── hdb3_decoder.py
│   ├── pcm_decoder.py
│   └── delta_decoder.py
├── analog/
│   ├── pcm.py
│   └── dm.py
└── tests/
    └── test_roundtrip.py
~~~

See SPECIFICATION.md for algorithm conventions, assumptions, complexity, and acknowledgement.
