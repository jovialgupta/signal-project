def longest_palindrome(data):
    if not data:
        return ""

    # Add separators so odd and even length palindromes
    # can be handled in the same way.
    transformed = '^#' + '#'.join(data) + '#$'

    radius = [0] * len(transformed)
    center = 0
    right = 0

    max_length = 0
    max_center = 0

    for i in range(1, len(transformed) - 1):

        mirror = 2 * center - i

        if i < right:
            radius[i] = min(right - i, radius[mirror])

        while transformed[i + (1 + radius[i])] == transformed[i - (1 + radius[i])]:
            radius[i] += 1

        if i + radius[i] > right:
            center = i
            right = i + radius[i]

        if radius[i] > max_length:
            max_length = radius[i]
            max_center = i

    start = (max_center - max_length) // 2

    return data[start:start + max_length]


if __name__ == "__main__":
    data = "101100101"
    result = longest_palindrome(data)

    print("Digital data:", data)
    print("Longest palindrome:", result)