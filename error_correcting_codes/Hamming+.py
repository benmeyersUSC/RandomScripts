import numpy as np
import functools

# bits = np.random.randint(0, 2, 16)
# print(f"Enumerated bits:\n{bits}")
#
# hamming_index = functools.reduce(lambda x, y: x ^ y, [i for i, bit in list(enumerate(bits)) if bit])
# print(f"Erroneous index: {hamming_index}")

def hamming(length):
    bits = np.random.randint(0, 2, length)
    print(f"INPUT:\n{bits}")

    hamming_index = functools.reduce(lambda x, y: x ^ y, [i for i, bit in list(enumerate(bits)) if bit])

    if hamming_index >= length:
        raise Exception("Message had 2 errors, try randomly generating a shorter one...")
    bits[hamming_index] = bits[hamming_index] ^ 1

    highlight = np.random.randint(0, 1, length)
    highlight[hamming_index] = 1

    highlight = " " * (1 + (2 * hamming_index)) + "*"

    print(f"\nCORRECTED (error at {hamming_index}): \n{highlight}\n{bits}")


if __name__ == "__main__":
    hamming(27)