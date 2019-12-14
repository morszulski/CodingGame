import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

ii = int(input())
nb = int(input())

print(ii, nb, file=sys.stderr)

lines: list = list()

for i in range(nb):
    line = input()
    line = list(line)
    lines.append(line)


# [print(ii, l, file=sys.stderr) for l in lines]


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def rotate_clockwise(lines):
    lines = list(zip(*reversed(lines)))
    return lines


def rotate_anti_clockwise(lines):
    lines = list(reversed(list(zip(*lines))))
    return lines


def move(len, c, r):
    c_new = (c + len) % nb
    r_new = int((r + (int((c + len) / nb))) % nb)
    return c_new, r_new


r: int = 0
c: int = 0
dir: int = 0
step: int = 1
loop_det: list = list()

while step <= ii:
    letter = lines[r][c]

    if letter not in ('@', '#'):
        loop_str = "{}{}{}{}".format(letter, dir, r, c)
        if loop_str in loop_det:
            loop_index = loop_det.index(loop_str)
            loop_len = len(loop_det) - loop_index
            loop_offset = (ii - loop_index) % loop_len
            if loop_offset == 0: loop_offset = loop_len
            print(loop_det, file=sys.stderr)
            print(f"ii{ii} step{step} len{loop_len} index{loop_index} offset{loop_offset}", file=sys.stderr)
            print(((ii - loop_index) % loop_len), file=sys.stderr)
            letter = loop_det[loop_offset + loop_index - 1][0]
            break
        else:
            loop_det.append(loop_str)
        c, r = move(ord(letter.capitalize()) - ord('A') + 1, c, r)
        step += 1

    if letter == '@':
        lines = rotate_anti_clockwise(lines)
        dir -= 1
        if dir <= 0:
            dir = 3
        continue
    if letter == '#':
        lines = rotate_clockwise(lines)
        dir = (dir + 1) % 4
        continue

print(letter)
