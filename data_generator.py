
import random


def generate_random_bits(length=16):
    """Generate a completely random binary string."""
    if length <= 0:
        raise ValueError("Length must be positive")

    return "".join(random.choice("01") for _ in range(length))


def generate_bits_with_zero_run(length=16, zero_count=8):
    """Generate random bits containing at least the requested zero run."""
    if length <= 0:
        raise ValueError("Length must be positive")

    if zero_count <= 0 or zero_count > length:
        raise ValueError("zero_count must be between 1 and length")

    # Reserve a position for the required consecutive zeros.
    start = random.randint(0, length - zero_count)

    bits = [
        random.choice("01")
        for _ in range(length)
    ]

    bits[start:start + zero_count] = ["0"] * zero_count

    return "".join(bits)


def longest_palindrome(bits):
    """Return the longest contiguous palindromic substring."""

    if not bits:
        return ""

    # Manacher's algorithm: O(n) time.
    transformed = "^#" + "#".join(bits) + "#$"
    radius = [0] * len(transformed)

    center = 0
    right = 0

    best_center = 0
    best_length = 0

    for i in range(1, len(transformed) - 1):
        mirror = 2 * center - i

        if i < right:
            radius[i] = min(right - i, radius[mirror])

        while (
            transformed[i + 1 + radius[i]]
            == transformed[i - 1 - radius[i]]
        ):
            radius[i] += 1

        if i + radius[i] > right:
            center = i
            right = i + radius[i]

        if radius[i] > best_length:
            best_length = radius[i]
            best_center = i

    start = (best_center - best_length) // 2

    return bits[start:start + best_length]


def generate_data(mode="random", length=16, zero_count=8):
    """Generate bits and return them with their longest palindrome."""

    if mode == "random":
        bits = generate_random_bits(length)

    elif mode == "zeros":
        bits = generate_bits_with_zero_run(length, zero_count)

    else:
        raise ValueError("Mode must be 'random' or 'zeros'")

    palindrome = longest_palindrome(bits)

    return bits, palindrome


if __name__ == "__main__":
    print("1. Random binary data")
    print("2. Data containing consecutive zeros")

    choice = input("Choose a mode: ").strip()

    try:
        length = int(input("Enter sequence length (default 16): ") or "16")

        if choice == "1":
            bits, palindrome = generate_data("random", length)

        elif choice == "2":
            zero_count = int(
                input("Consecutive zeros (4 or 8): ").strip()
            )

            if zero_count not in (4, 8):
                raise ValueError("Choose either 4 or 8 zeros")

            bits, palindrome = generate_data(
                "zeros", length, zero_count
            )

        else:
            raise ValueError("Choose option 1 or 2")

        print("Generated bits:", bits)
        print("Longest palindrome:", palindrome)
        print("Palindrome length:", len(palindrome))

    except ValueError as error:
        print("Input error:", error)
