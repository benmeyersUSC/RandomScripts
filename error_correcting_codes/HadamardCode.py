import math
import random
import pandas as pd
import numpy as np

green_print = lambda x: f"\033[30;42m{x}\033[0m"
red_print = lambda x: f"\033[30;41m{x}\033[0m"
yellow_print = lambda x: f"\033[30;43m{x}\033[0m"
blue_print = lambda x: f"\033[30;44m{x}\033[0m"


def int_to_bin_list(x: int, pad_len):
    if x == 0:
        return [0] * pad_len

    res = []
    while x > 0:
        res.append(x % 2)
        x //= 2

    res = res[::-1]
    res = [0] * (pad_len - len(res)) + res

    return res


def print_bit_flip(c):
    lc = [x for x in c]
    for i in range(len(lc)):
        if "y" in str(lc[i]).lower():
            lc[i] = red_print("*")
        else:
            lc[i] = green_print(" ")
    return "".join(lc)


def get_next_p_of_2(n):
    while not n & (n - 1) == 0:
        n += 1
    return n


def generate_basic_hadamard_matrix(n):
    """
    Generate a basic Hadamard matrix recursively

    Args:
    n (int): Order of the Hadamard matrix

    Returns:
    numpy.ndarray: Hadamard matrix
    """
    # Base case
    if n == 0:
        return np.array([[1]])

    # Recursive generation
    H_prev = generate_basic_hadamard_matrix(n - 1)

    # Construct new Hadamard matrix
    H_new = np.block([
        [H_prev, H_prev],
        [H_prev, -H_prev]
    ])

    return H_new


def flip_random_slots(arr, n):
    # Ensure N does not exceed the array length
    n = min(n, len(arr))

    # Randomly select N unique indices
    indices_to_flip = np.random.choice(len(arr), size=n, replace=False)

    # Flip the values at the chosen indices
    arr[indices_to_flip] = 1 - arr[indices_to_flip]

    return arr


# def run_hadamard_example(length, flip_bits=0):
#     msg = np.random.randint(0, 2, length)
#     print(f"Randomly Generated Message:\n{green_print(msg)}")
#
#     # matrix_order = get_next_p_of_2(length)
#
#     flip_bits = min(flip_bits, (matrix_order - 1) // 2)
#
#     H = generate_basic_hadamard_matrix(math.log(matrix_order, 2))
#     # print(f"Hadamard Matrix:\n{pd.DataFrame(H)}")
#     print(f"Hadamard Matrix:\n{pd.DataFrame(H).to_string(index=False, header=False)}")
#
#     msg = np.pad(
#         msg,
#         (0, matrix_order - len(msg)),  # Padding (left=0, right=matrix_order - len(msg))
#         mode='constant'
#     )
#     print(f"Padded Message: \n{green_print(msg)}")
#
#     enc_message = np.dot(msg, H)
#     print(f"Intermediate Encoded Message: \n{enc_message}")
#
#     # transformed_message = (enc_message > 0).astype(int)
#     transformed_message = (enc_message >= 0).astype(int)
#     print(f"Transformed Encoded Message For Transit: \n{transformed_message}")
#
#     if flip_bits > 0:
#         transformed_message = flip_random_slots(transformed_message, flip_bits)
#         print(f"Erroneous Message ({flip_bits} errors):\n{transformed_message}")
#
#     print(f"Decoding: \n{transformed_message}")
#
#     correlations = np.dot(transformed_message, H)
#     decoded_index = np.argmax(np.abs(correlations))
#     decoded_message = H[decoded_index]
#     print(f"Decoded Message: {decoded_message}")

def hamming_distance(a, b):
    return np.sum(np.abs(a - b))


def hadamard(length):
    msg = np.random.randint(0, 2, length)
    print(f"Randomly Generated Message:\n{green_print(msg)}")

    H = generate_h_matrix(length)

    print(f"Hadamard Matrix:\n{pd.DataFrame(H).to_string(index=False, header=False)}")

    encoded = (msg @ H) % 2

    cleancoded = encoded.copy()

    print(f"Encoded message:\n{encoded}")

    n = 2 ** length
    d = n // 2
    error_max = (d - 1) // 2

    errors = random.randint(1, error_max)

    transit = flip_random_slots(encoded, errors)
    print(f"{errors} errors!:\n{transit}")

    code_words = []
    for row in H.T:
        code_words.append((row @ H) % 2)

    code_word_matrix = np.array(code_words)

    print(f"Code Word Matrix:\n{pd.DataFrame(code_word_matrix).to_string(index=False, header=False)}")

    affs = []
    for col in code_word_matrix:
        affs.append(int(hamming_distance(transit, col)))

    print(affs)

    found = code_word_matrix[np.argmin(affs)]

    print(found)

    print(np.all(cleancoded == found))
    return np.all(cleancoded == found)


def generate_h_matrix(n):
    ls = np.array([int_to_bin_list(i, n) for i in range(2 ** n)])

    return ls.T


if __name__ == "__main__":
    hadamard(3)

    """
    a single bitflip will correspond to half of the bits in the code word flipping
    because that bit appears in half the code words
    """
