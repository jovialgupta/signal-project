import matplotlib.pyplot as plt


def nrz_l_encode(bits):
    signal = []

    for bit in bits:
        if bit == '1':
            signal.append(1)
        else:
            signal.append(-1)

    return signal


def nrz_l_decode(signal):
    bits = ''

    for level in signal:
        if level > 0:
            bits += '1'
        else:
            bits += '0'

    return bits

def plot_nrz_l(bits, signal):
    time = list(range(len(bits) + 1))

    signal_plot = signal + [signal[-1]]

    plt.step(time, signal_plot, where='post')

    plt.title("NRZ-L Encoding")
    plt.xlabel("Bit")
    plt.ylabel("Voltage")

    plt.yticks([-1, 1], ['0', '1'])
    plt.grid(True)

    for i, bit in enumerate(bits):
        plt.text(i + 0.5, 1.2, bit, ha='center')

    plt.show()

if __name__ == "__main__":
    data = "10110010"

    encoded = nrz_l_encode(data)
    decoded = nrz_l_decode(encoded)

    print("Original data:", data)
    print("NRZ-L signal:", encoded)
    print("Decoded data:", decoded)

    plot_nrz_l(data, encoded)

def nrz_i_encode(bits):
    signal = []
    current_level = -1

    for bit in bits:
        if bit == '1':
            current_level = -current_level

        signal.append(current_level)

    return signal

def nrz_i_decode(signal):
    bits = ''
    previous_level = -1

    for level in signal:
        if level != previous_level:
            bits += '1'
        else:
            bits += '0'

        previous_level = level

    return bits

if __name__ == "__main__":
    data = "10110010"

    encoded = nrz_i_encode(data)
    decoded = nrz_i_decode(encoded)

    print("Original data:", data)
    print("NRZ-I signal:", encoded)
    print("Decoded data:", decoded)

def plot_nrz_i(bits, signal):
    time = list(range(len(bits) + 1))
    signal_plot = signal + [signal[-1]]

    plt.step(time, signal_plot, where='post')

    plt.title("NRZ-I Encoding")
    plt.xlabel("Bit")
    plt.ylabel("Voltage")

    plt.yticks([-1, 1], ['-1', '+1'])
    plt.grid(True)

    for i, bit in enumerate(bits):
        plt.text(i + 0.5, 1.2, bit, ha='center')

    plt.show()

if __name__ == "__main__":
    data = "10110010"

    # NRZ-L
    nrz_l_signal = nrz_l_encode(data)
    nrz_l_decoded = nrz_l_decode(nrz_l_signal)

    print("NRZ-L signal:", nrz_l_signal)
    print("NRZ-L decoded:", nrz_l_decoded)

    plot_nrz_l(data, nrz_l_signal)

    # NRZ-I
    nrz_i_signal = nrz_i_encode(data)
    nrz_i_decoded = nrz_i_decode(nrz_i_signal)

    print("NRZ-I signal:", nrz_i_signal)
    print("NRZ-I decoded:", nrz_i_decoded)

    plot_nrz_i(data, nrz_i_signal)