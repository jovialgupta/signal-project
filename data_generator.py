
import random


def generate_random_bits(length=16):
    """Generate a random binary sequence."""
    if length <= 0:
        raise ValueError("Length must be positive.")

    return "".join(random.choice("01") for _ in range(length))


def generate_bits_with_zero_run(length=16, zero_count=8):
    """Generate a binary sequence containing 4 or 8 consecutive zeros."""
    if length <= 0:
        raise ValueError("Length must be positive.")

    if zero_count not in (4, 8):
        raise ValueError("zero_count must be 4 or 8.")

    if length < zero_count:
        raise ValueError("Length must be at least zero_count.")

    bits = [
        random.choice("01")
        for _ in range(length)
    ]

    start = random.randint(0, length - zero_count)
    bits[start:start + zero_count] = ["0"] * zero_count

    return "".join(bits)


def longest_palindrome(bits):
    """Find the longest palindromic substring using Manacher's algorithm."""
    if not bits:
        return ""

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
    """Generate data and return it with its longest palindrome."""
    if mode == "random":
        bits = generate_random_bits(length)
    elif mode == "zeros":
        bits = generate_bits_with_zero_run(length, zero_count)
    else:
        raise ValueError("Mode must be 'random' or 'zeros'.")

    return bits, longest_palindrome(bits)


if __name__ == "__main__":
    print("\n--- Digital Data Generator ---")
    print("1. Random binary sequence")
    print("2. Sequence containing four consecutive zeros")
    print("3. Sequence containing eight consecutive zeros")

    choice = input("Choose (1-3): ").strip()

    try:
        length = int(input("Sequence length (default 16): ") or "16")

        if choice == "1":
            bits, palindrome = generate_data("random", length)
        elif choice in ("2", "3"):
            zero_count = 4 if choice == "2" else 8
            bits, palindrome = generate_data(
                "zeros",
                length,
                zero_count,
            )
        else:
            raise ValueError("Choose 1, 2, or 3.")

        print("\nGenerated bits:", bits)
        print("Longest palindrome:", palindrome)
        print("Palindrome length:", len(palindrome))

    except ValueError as error:
        print("Input error:", error)
