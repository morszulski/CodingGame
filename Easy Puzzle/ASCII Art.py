import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


l = int(input())
h = int(input())
t = input()
rows: list = list()
for i in range(h):
    row = input()
    rows.append(row)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

out_rows: list = list()
for h1 in range(h):
    out_row: list = list()
    for letter in t:
        letter = letter.capitalize()
        letter_index = ord(letter)
        if ord('A') <= letter_index <= ord('Z'):
            pass
        else:
            letter_index = ord('Z') + 1
        letter_index -= ord('A')
        start_pos = letter_index * l

        out_row.append(rows[h1][start_pos:start_pos + l])

    print(''.join(out_row))
