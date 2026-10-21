\# Digital Signal Encoder and Decoder



\## Project Overview



This project implements digital line encoding, decoding, and analog-to-digital signal techniques using Python. It also provides graphical visualization of signals.



\## Features



\### Digital Line Encoding

\- NRZ-L (Non-Return-to-Zero Level)

\- NRZ-I (Non-Return-to-Zero Invert)

\- Manchester Encoding

\- Differential Manchester Encoding

\- Alternate Mark Inversion (AMI)

\- Bipolar with 8-Zero Substitution (B8ZS)

\- High-Density Bipolar 3 Zeros (HDB3)



\### Decoding

\- NRZ-L decoding

\- NRZ-I decoding

\- Manchester decoding

\- Differential Manchester decoding

\- AMI decoding



\### Analog Signal Techniques

\- Pulse Code Modulation (PCM)

\- Delta Modulation (DM)



\### Visualization

\- Graphical signal waveforms using Matplotlib



\## Technologies Used

\- Python

\- NumPy

\- Matplotlib



\## Installation



Install the required packages:



```bash

python -m pip install -r requirements.txt

```



\## How to Run



Run the main program from the project directory:



```bash

python main.py

```



Choose an option from the menu and follow the prompts.



\## Example



For NRZ-L, enter option `1` and the bit sequence `10110`.



The program displays the encoded signal and decoded bit sequence.



\## Project Structure



```text

signal-project/

├── main.py

├── plotting.py

├── requirements.txt

├── README.md

├── encoders/

│   ├── nrz/

│   ├── manchester/

│   ├── ami.py

│   ├── b8zs.py

│   └── hdb3.py

├── decoders/

│   ├── nrz\_decoder.py

│   ├── manchester\_decoder.py

│   └── ami\_decoder.py

└── analog/

&#x20;   ├── pcm.py

&#x20;   └── dm.py

```



\## Team Project



This project demonstrates digital signal encoding and decoding, PCM, Delta Modulation, and signal visualization.



