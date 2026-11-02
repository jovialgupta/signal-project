# Digital Signal Encoder and Decoder — Specification

## 1. Language and libraries
- **Language:** Python 3
- **Libraries:** NumPy (numerical arrays), Matplotlib (waveform plots), Pillow (reading waveform PNG pixels), and Python standard-library modules (random, unittest, tempfile, pathlib).

## 2. Functional scope
- Generate random binary streams, streams containing at least four consecutive zeros, streams containing at least eight consecutive zeros, or accept a manually entered stream.
- Find the **longest contiguous palindromic substring** using Manacher's algorithm in **O(n) time and O(n) space**. A separate dynamic-programming helper also reports the longest palindromic subsequence in O(n²) time and O(n²) space, because the assignment wording can be interpreted either way.
- Encode digital data using NRZ-L, NRZ-I, Manchester, Differential Manchester, or AMI. When AMI is selected, the user can choose no scrambling, B8ZS, or HDB3.
- Accept analog samples and perform PCM or Delta Modulation (DM). Decode PCM to reconstructed quantized samples and DM to its staircase signal. PCM/DM bitstreams can optionally be passed to a line-coding scheme.
- For extra credit, save the encoded waveform as a calibrated PNG and recover its signal levels by examining image pixels. The original encoded array is not passed to the image decoder.

## 3. Assumptions and conventions
- Digital input contains only 0 and 1.
- NRZ-L maps 1 to +1 and 0 to -1. NRZ-I starts at -1 and transitions for each 1.
- Manchester maps 1 to (+1, -1) and 0 to (-1, +1). Differential Manchester starts at -1, always transitions in the middle, and makes a beginning transition for 0.
- AMI starts with a previous pulse polarity of -1; successive 1 pulses alternate polarity. B8ZS and HDB3 use the same initial polarity.
- PCM uses uniform quantization over the minimum and maximum values of the supplied samples. The bit depth is selected by the user.
- DM uses a user-selected positive step size. The initial staircase value is the first input sample; a 1 steps upward and a 0 steps downward.
- User-entered analog samples are treated as equally spaced and must be finite numbers.
- Image decoding supports the three plotted levels (-1, 0, +1); the PNG is generated with fixed calibration and one equal-width cell per encoded signal level.

## 4. How to run
Install dependencies:
~~~bash
python -m pip install numpy matplotlib pillow
~~~
Run the interactive program:
~~~bash
python main.py
~~~
Run regression tests:
~~~bash
python -m unittest discover -s tests
~~~

## 5. References and acknowledgement
- Course lecture notes and assignment specification for line coding, scrambling, PCM, and DM conventions.
- Manacher, G. (1975), “A new linear-time 'on-line' algorithm for finding the smallest initial palindrome of a string,” *Journal of the ACM*, 22(3), 346–351.
- NumPy documentation: https://numpy.org/doc/
- Matplotlib documentation: https://matplotlib.org/stable/
- Pillow documentation: https://pillow.readthedocs.io/
- **AI assistance acknowledgement:** ChatGPT was used for code-review guidance, refactoring suggestions, and drafting regression-test cases. The project team is responsible for understanding, verifying, and explaining the submitted implementation.
