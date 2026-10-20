import matplotlib.pyplot as plt

def plot_digital_signal(signal, title="Digital Signal"):
    plt.figure(figsize=(8,3))
    plt.step(range(len(signal)), signal, where="post")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
