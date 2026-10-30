
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
    n = len(bits)

    if n == 0:
        return ""

    # dp[i][j] = length of the longest palindromic
    # subsequence in bits[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # A single character is always a palindrome
    for i in range(n):
        dp[i][i] = 1

    # Consider substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if bits[i] == bits[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(
                    dp[i + 1][j],
                    dp[i][j - 1]
                )

    # Reconstruct the actual palindrome
    left = 0
    right = n - 1
    first = []
    last = []

    while left <= right:
        if left == right:
            first.append(bits[left])
            break

        if bits[left] == bits[right]:
            first.append(bits[left])
            last.append(bits[right])
            left += 1
            right -= 1
        elif dp[left + 1][right] >= dp[left][right - 1]:
            left += 1
        else:
            right -= 1

    return "".join(first + last[::-1])

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
