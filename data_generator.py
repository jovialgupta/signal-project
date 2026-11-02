"""Digital data generation and palindrome utilities."""

import random


def generate_random_bits(length=16):
    """Generate a random binary sequence in O(length) time."""
    if length <= 0:
        raise ValueError("Length must be positive.")
    return "".join(random.choice("01") for _ in range(length))


def generate_bits_with_zero_run(length=16, zero_count=8):
    """Generate bits containing at least 4 or 8 consecutive zeros."""
    if length <= 0:
        raise ValueError("Length must be positive.")
    if zero_count not in (4, 8):
        raise ValueError("zero_count must be 4 or 8.")
    if length < zero_count:
        raise ValueError("Length must be at least zero_count.")

    bits = [random.choice("01") for _ in range(length)]
    start = random.randint(0, length - zero_count)
    bits[start:start + zero_count] = ["0"] * zero_count
    return "".join(bits)


def longest_palindrome(bits):
    """Return the longest contiguous palindromic substring using Manacher.

    Time complexity: O(n). Space complexity: O(n).
    """
    n = len(bits)
    if n == 0:
        return ""

    odd = [0] * n
    left, right = 0, -1
    best_start, best_length = 0, 0

    for center in range(n):
        radius = (
            1
            if center > right
            else min(odd[left + right - center], right - center + 1)
        )

        while (
            center - radius >= 0
            and center + radius < n
            and bits[center - radius] == bits[center + radius]
        ):
            radius += 1

        odd[center] = radius
        length = 2 * radius - 1
        start = center - radius + 1
        if length > best_length:
            best_start, best_length = start, length

        if center + radius - 1 > right:
            left, right = center - radius + 1, center + radius - 1

    even = [0] * n
    left, right = 0, -1

    for center in range(n):
        radius = (
            0
            if center > right
            else min(even[left + right - center + 1], right - center + 1)
        )

        while (
            center - radius - 1 >= 0
            and center + radius < n
            and bits[center - radius - 1] == bits[center + radius]
        ):
            radius += 1

        even[center] = radius
        length = 2 * radius
        start = center - radius
        if length > best_length:
            best_start, best_length = start, length

        if center + radius - 1 > right:
            left, right = center - radius, center + radius - 1

    return bits[best_start:best_start + best_length]


def longest_palindromic_subsequence(bits):
    """Return a longest palindromic subsequence in O(n^2) time and space.

    This is provided separately because 'palindromic sequence' can also mean
    a subsequence whose selected characters need not be adjacent.
    """
    n = len(bits)
    if n == 0:
        return ""

    dp = [[0] * n for _ in range(n)]
    for index in range(n):
        dp[index][index] = 1

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if bits[start] == bits[end]:
                dp[start][end] = (
                    2 if length == 2 else dp[start + 1][end - 1] + 2
                )
            else:
                dp[start][end] = max(
                    dp[start + 1][end],
                    dp[start][end - 1],
                )

    left, right = 0, n - 1
    first_half, second_half = [], []

    while left <= right:
        if left == right:
            first_half.append(bits[left])
            break
        if bits[left] == bits[right]:
            first_half.append(bits[left])
            second_half.append(bits[right])
            left += 1
            right -= 1
        elif dp[left + 1][right] >= dp[left][right - 1]:
            left += 1
        else:
            right -= 1

    return "".join(first_half + second_half[::-1])


def generate_data(mode="random", length=16, zero_count=8):
    """Generate data and return it with its longest contiguous palindrome."""
    generators = {
        "random": lambda: generate_random_bits(length),
        "zeros": lambda: generate_bits_with_zero_run(length, zero_count),
    }
    try:
        bits = generators[mode]()
    except KeyError as error:
        raise ValueError("Mode must be 'random' or 'zeros'.") from error
    return bits, longest_palindrome(bits)


if __name__ == "__main__":
    print("\\n--- Digital Data Generator ---")
    print("1. Random binary sequence")
    print("2. Sequence containing four consecutive zeros")
    print("3. Sequence containing eight consecutive zeros")

    choice = input("Choose (1-3): ").strip()
    try:
        length = int(input("Sequence length (default 16): ") or "16")
        options = {
            "1": ("random", 8),
            "2": ("zeros", 4),
            "3": ("zeros", 8),
        }
        mode, zero_count = options[choice]
        bits, palindrome = generate_data(mode, length, zero_count)
        subsequence = longest_palindromic_subsequence(bits)

        print("\\nGenerated bits:", bits)
        print("Longest contiguous palindrome:", palindrome)
        print("Longest palindromic subsequence:", subsequence)
    except (KeyError, ValueError) as error:
        print("Input error:", error)
