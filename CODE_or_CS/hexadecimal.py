def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


def decimal_to_hex(decimal_number: int):
    if decimal_number == 0:
        return '0'

    hex_digits = '0123456789ABCDEF'
    hex_num = ''

    while decimal_number > 0:
        remainder = decimal_number % 16
        # print(f'{decimal_number} % 16: {remainder}')
        hex_num = hex_digits[remainder] + hex_num
        # print(f'current hex: {hex_num}')
        # print(f'new decimal is {decimal_number} // 16: {decimal_number//16}')
        decimal_number = decimal_number // 16

    return hex_num

def binary_to_hex(binary_number):
    if binary_number == '0':
        return '0'

    dec_number = 0

    ind = 0
    while len(binary_number) > 0:
        dec_number += int(binary_number[-1]) * 2 ** (ind)
        binary_number = binary_number[:-1]
        ind += 1

    return decimal_to_hex(dec_number)

print(decimal_to_hex(91))

print(decimal_to_binary(91))

print(binary_to_hex('1011011'))
