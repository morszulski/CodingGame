import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

ENCODE_DICT: dict = {
    '0': '00',
    '1': '0',
}

ENCODE_CHAR: str = '0'
SEP_CHAR: str = ' '


def message_2_bin_string(message: str):
    bin_str: list = list()
    for char in message:
        bin_number = ord(char)
        bin_str.append(f'{bin_number:07b}')
    bin_str = ''.join(bin_str)
    return bin_str


def bin_2_series(bin_str: str):
    series: list = list()
    first_char = bin_str[0]
    serie_length = 0
    for char in bin_str:
        if char == first_char:
            serie_length += 1
        else:
            series.append((serie_length, first_char))
            serie_length = 1
            first_char = char
    series.append((serie_length, first_char))
    return series


message = input()
bin_str = message_2_bin_string(message)
series = bin_2_series(bin_str)

answer: list = list()
for s_l, s_v in series:
    answer.extend([ENCODE_DICT.get(s_v), ENCODE_CHAR * s_l])

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(SEP_CHAR.join(answer))
