import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def sum_n(n: int = 0):
    """
    >>> sum_n(3)
    6
    """
    s = 0
    for i in range(0, n + 1):
        s += i
    return s


def decode_message(message):
    segment = 0
    sum = 0
    while sum < len(message):
        segment += 1
        sum += segment

    segment_len = len(message) + segment - sum
    lacking_segment = segment - segment_len

    if segment % 2 == 0:
        from_left = True
        start = 0
    else:
        from_left = False
        start = len(message) - segment_len

    result = ''

    while segment > 0:
        result = ''.join((message[start: start + segment_len], result))
        segment -= 1
        segment_len = segment
        if from_left:
            start += sum_n(segment) + 1 - lacking_segment
        else:
            start -= sum_n(segment)
        from_left = not from_left
        lacking_segment = 0
    return result


def encode_message(message):
    l = 1
    i = 0
    begin = False
    result = ''
    while i <= len(message):
        if begin:
            result = ''.join((message[i: i + l], result))
        else:
            result = ''.join((result, message[i: i + l]))
        i += l
        l += 1
        begin = not begin
    return result


def encode_decode(message, n=1):
    """
    >>> encode_decode('123')
    '123'
    >>> encode_decode('1',10)
    '1'
    >>> encode_decode('1234567890asdfghjkl',3)
    '1234567890asdfghjkl'
    >>> encode_decode('1 2 3 4 5 6 7 8 9 0 11',6)
    '1 2 3 4 5 6 7 8 9 0 11'
    """
    for i in range(0, n):
        message = encode_message(message)
    for i in range(0, n):
        message = decode_message(message)
    return message


if __name__ == '__main__':
    n = int(input())
    message = input()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if n > 0:
        for i in range(0, n):
            message = decode_message(message)
    else:
        for i in range(0, abs(n)):
            message = encode_message(message)

    print(message)
