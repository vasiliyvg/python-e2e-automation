hex_numbers = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}


def hex_to_dec(hex_num):
    for char in hex_num:
        if char not in hex_numbers:
            return None

        if len(hex_num) == 3:
            return hex_numbers[hex_num[0]] * 256 + hex_numbers[hex_num[1]] * 16 + hex_numbers[hex_num[2]]
        if len(hex_num) == 2:
            return hex_numbers[hex_num[0]] * 16 * hex_numbers[hex_num[1]]
        if len(hex_num) == 1:
            return hex_numbers[hex_num[0]]


print(hex_to_dec('A'))
