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