import matplotlib.pyplot as plt


# ==================== NRZ-L ENCODER ====================

def nrz_l_encode(bits):
    if any(bit not in '01' for bit in bits):
        raise ValueError("Input must contain only 0s and 1s")

    signal = []

    for bit in bits:
        if bit == '1':
            signal.append(1)
        else:
            signal.append(-1)

    return signal


# ==================== NRZ-L DECODER ====================

def nrz_l_decode(signal):
    bits = ''

    for level in signal:
        if level > 0:
            bits += '1'
        else:
            bits += '0'

    return bits


# ==================== NRZ-L GRAPH ====================

def plot_nrz_l(bits, signal):
    if not signal:
        print("Cannot plot an empty signal.")
        return

    time = list(range(len(signal) + 1))
    signal_plot = signal + [signal[-1]]

    plt.figure()
    plt.step(time, signal_plot, where='post')

    plt.title("NRZ-L Encoding")
    plt.xlabel("Time (Bit Interval)")
    plt.ylabel("Voltage Level")

    plt.yticks([-1, 1], ['-1 (Bit 0)', '+1 (Bit 1)'])
    plt.xticks(time)
    plt.grid(True)

    for i, bit in enumerate(bits):
        plt.text(i + 0.5, 1.15, bit, ha='center')

    plt.tight_layout()
    plt.show()


# ==================== NRZ-I ENCODER ====================

def nrz_i_encode(bits):
    if any(bit not in '01' for bit in bits):
        raise ValueError("Input must contain only 0s and 1s")

    signal = []
    current_level = -1

    for bit in bits:
        if bit == '1':
            current_level = -current_level

        signal.append(current_level)

    return signal


# ==================== NRZ-I DECODER ====================

def nrz_i_decode(signal):
    bits = ''
    previous_level = -1

    for level in signal:
        if level not in (-1, 1):
            raise ValueError("Signal levels must be -1 or +1")

        if level != previous_level:
            bits += '1'
        else:
            bits += '0'

        previous_level = level

    return bits


# ==================== NRZ-I GRAPH ====================

def plot_nrz_i(bits, signal):
    if not signal:
        print("Cannot plot an empty signal.")
        return

    time = list(range(len(signal) + 1))
    signal_plot = signal + [signal[-1]]

    plt.figure()
    plt.step(time, signal_plot, where='post')

    plt.title("NRZ-I Encoding")
    plt.xlabel("Time (Bit Interval)")
    plt.ylabel("Voltage Level")

    plt.yticks([-1, 1], ['-1', '+1'])
    plt.xticks(time)
    plt.grid(True)

    for i, bit in enumerate(bits):
        plt.text(i + 0.5, 1.15, bit, ha='center')

    plt.tight_layout()
    plt.show()


# ==================== MAIN PROGRAM ====================

if __name__ == "__main__":

    data = "10110010"

    print("Original data:", data)
    print()

    # NRZ-L encoding and decoding
    nrz_l_signal = nrz_l_encode(data)
    nrz_l_decoded = nrz_l_decode(nrz_l_signal)

    print("----- NRZ-L -----")
    print("Encoded signal:", nrz_l_signal)
    print("Decoded data:", nrz_l_decoded)
    print("Decoding successful:", data == nrz_l_decoded)
    print()

    # NRZ-I encoding and decoding
    nrz_i_signal = nrz_i_encode(data)
    nrz_i_decoded = nrz_i_decode(nrz_i_signal)

    print("----- NRZ-I -----")
    print("Encoded signal:", nrz_i_signal)
    print("Decoded data:", nrz_i_decoded)
    print("Decoding successful:", data == nrz_i_decoded)

    # Display graphs
    plot_nrz_l(data, nrz_l_signal)
    plot_nrz_i(data, nrz_i_signal)
