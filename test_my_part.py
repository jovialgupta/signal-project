from data_generator import generate_random_data
from palindrome import longest_palindrome
from line_encoding import nrz_l_encode, nrz_l_decode
from line_encoding import nrz_i_encode, nrz_i_decode


# Generate random digital data
data = generate_random_data(20)

print("Original data:", data)

# Find longest palindrome
palindrome = longest_palindrome(data)

print("Longest palindrome:", palindrome)

# NRZ-L
nrz_l_signal = nrz_l_encode(data)
nrz_l_decoded = nrz_l_decode(nrz_l_signal)

print("NRZ-L signal:", nrz_l_signal)
print("NRZ-L decoded:", nrz_l_decoded)

# NRZ-I
nrz_i_signal = nrz_i_encode(data)
nrz_i_decoded = nrz_i_decode(nrz_i_signal)

print("NRZ-I signal:", nrz_i_signal)
print("NRZ-I decoded:", nrz_i_decoded)


# Check whether decoding is correct
assert nrz_l_decoded == data
assert nrz_i_decoded == data

print("\nAll tests passed!")