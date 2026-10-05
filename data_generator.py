import random


def generate_random_data(length):
    if length <= 0:
        raise ValueError("Length must be greater than 0")

    return ''.join(random.choice('01') for _ in range(length))

def generate_data_with_zeros(length, zero_count):
    if length < zero_count:
        raise ValueError("Length must be at least zero_count")

    bits = list(generate_random_data(length))

    start = random.randint(0, length - zero_count)

    for i in range(start, start + zero_count):
        bits[i] = '0'

    return ''.join(bits)

if __name__ == "__main__":
    data = generate_random_data(20)
    print("Random data:", data)

    data_4 = generate_data_with_zeros(20, 4)
    print("Data with 4 consecutive zeros:", data_4)

    data_8 = generate_data_with_zeros(20, 8)
    print("Data with 8 consecutive zeros:", data_8)