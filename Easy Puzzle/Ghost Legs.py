import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
t = input().split('  ')

cursors = dict()
for c in range(len(t)):
    cursors[t[c]] = int(c * 3)

for i in range(1, h - 1):
    line = input()
    # print(line, file=sys.stderr)
    # print(cursors, file=sys.stderr)
    for c in cursors:
        pos = cursors[c]
        if line[pos - 1] == '-':
            cursors[c] -= 3
        elif pos < len(line)-1:
            if line[pos + 1] == '-':
                cursors[c] += 3
    # print(cursors, file=sys.stderr)

line = input()
for c in cursors:
    print(f'{c}{line[cursors[c]]}')

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
