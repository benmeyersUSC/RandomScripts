def cOR(x, y):
    if x == '0' and y == '0':
        return '0'
    if x == '1' and y == '1':
        return '1'
    if x == '1' and y == '0':
        return '1'
    if x == '0' and y == '1':
        return '1'

def three_input_nor(a, b, c):
    if not (a in '01' and b in '01' and c in '01'):
        raise ValueError("All inputs must be '0' or '1'")
    return '0' if a == '1' or b == '1' or c == '1' else '1'

def three_input_and(a, b, c):
    if not (a in '01' and b in '01' and c in '01'):
        raise ValueError("All inputs must be '0' or '1'")
    return '1' if a == '1' and b == '1' and c == '1' else '0'

def twos_complement(x):
    # Ensure the input is a valid 8-bit binary string
    if len(x) != 8 or not all(bit in '01' for bit in x):
        raise ValueError("Input must be an 8-bit binary string")

    # Invert the bits
    new_x = ''
    for i in x:
        if i == '0':
            new_x += '1'
        elif i == '1':
            new_x += '0'

    # Convert the inverted bits to an integer
    inverted_int = int(new_x, 2)

    # Add 1 to the inverted integer
    twos_complement_int = inverted_int + 1

    # Convert the result back to an 8-bit binary string
    twos_complement_bin = format(twos_complement_int, '08b')

    # Ensure the result is exactly 8 bits
    twos_complement_bin = twos_complement_bin[-8:]

    return twos_complement_bin

def binary_pad(x, n):
    while len(x) < n:
        x = '0' + x
    return x


def binary_to_decimal(binary_string):
    # Initialize the decimal result to 0
    decimal_number = 0

    # Iterate over the binary string
    for digit in binary_string:
        # Shift the current result to the left (equivalent to multiplying by 2)
        decimal_number = decimal_number * 2
        # Add the current digit (0 or 1) to the result
        decimal_number += int(digit)

    return decimal_number

def half_adder(x, y):
    sum = int(x) ^ int(y)
    carry = int(x) & int(y)

    return str(sum), str(carry)

def full_adder(x, y, c='0'):
    first_sum, first_carry = half_adder(x, y)
    second_sum, second_carry = half_adder(c, first_sum)

    sum = second_sum
    carry = cOR(first_carry, second_carry)

    return sum, carry

def eight_bit_adder(x, y, c='0'):
    x = binary_pad(x, 8)
    y = binary_pad(y, 8)

    sum = ''

    first_s, first_c = full_adder(x[-1], y[-1])
    sum += first_s

    second_s, second_c = full_adder(x[-2], y[-2], first_c)
    sum = second_s + sum

    third_s, third_c = full_adder(x[-3], y[-3], second_c)
    sum = third_s + sum

    fourth_s, fourth_c = full_adder(x[-4], y[-4], third_c)
    sum = fourth_s + sum

    fifth_s, fifth_c = full_adder(x[-5], y[-5], fourth_c)
    sum = fifth_s + sum

    sixth_s, sixth_c = full_adder(x[-6], y[-6], fifth_c)
    sum = sixth_s + sum

    seventh_s, seventh_c = full_adder(x[-7], y[-7], sixth_c)
    sum = seventh_s + sum

    eighth_s, eighth_c = full_adder(x[-8], y[-8], seventh_c)
    # sum = eighth_c + eighth_s + sum
    # if eighth_c == '1':
    #     print('RESULT TOO LARGE (>255), 8 LSBs:')
    sum = eighth_s + sum

    return sum

def eight_bit_add_or_sub(x, y, sub=False):
    x = binary_pad(x, 8)
    y = binary_pad(y, 8)

    if sub:
        print(f"{x} ({binary_to_decimal(x)}) - {y} ({binary_to_decimal(y)})")
        y = twos_complement(y)
        print(f"SUBTRACTION: y now = {y} ({binary_to_decimal(y)})")


    x7, y7 = x[0], y[0]

    output_sum = eight_bit_adder(x, y)
    print(f"Raw sum from addition ({x} ({binary_to_decimal(x)}) + {y} ({binary_to_decimal(y)})): {output_sum} = {binary_to_decimal(output_sum)}")
    output_sign = '0' if output_sum[0] == '1' else '1'

    if sub and x[0] != y[0] and output_sum[0] != x[0]:
        print('OVERFLOW! INVALID ANSWER')

    overflow_and = three_input_and(output_sign, x7, y7)
    overflow_nor = three_input_nor(output_sign, x7, y7)

    overflow = cOR(overflow_and, overflow_nor)
    # print(f"Overflow: {overflow}")

    if overflow == '1':
        print('OVERFLOW, invalid answer')

    # if output_sum[0] == '1':
    #     output_sum = '-' + twos_complement(output_sum)

    return output_sum, overflow

# eight_bit_add_or_sub('01111111', '100011', True)

print(binary_to_decimal(eight_bit_adder('10000011', '01111111')))
