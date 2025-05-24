def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

# Example
print("Decimal 13 to Binary:", decimal_to_binary(13))  # Output: 1101


def binary_to_decimal(b):
    decimal = 0
    b = b[::-1]  # reverse string
    for i in range(len(b)):
        decimal += int(b[i]) * (2 ** i)
    return decimal

# Example
print("Binary 1010 to Decimal:", binary_to_decimal("1010"))  # Output: 10

def hex_to_binary(hex_str):
    binary = ''
    for digit in hex_str.upper():
        binary += format(int(digit, 16), '04b')  # 4-bit binary
    return binary

# Example
print("Hexadecimal 2F to Binary:", hex_to_binary("2F"))  # Output: 00101111

def binary_to_hex(b):
    # Pad with 0s on the left to make length multiple of 4
    b = b.zfill((len(b) + 3) // 4 * 4)
    hex_str = ''
    for i in range(0, len(b), 4):
        group = b[i:i+4]
        hex_digit = format(int(group, 2), 'X')
        hex_str += hex_digit
    return hex_str

# Example
print("Binary 10110110 to Hex:", binary_to_hex("10110110"))  # Output: B6
