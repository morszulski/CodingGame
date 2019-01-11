import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
powers = list()
deltas = list()
for i in range(n):
    pi = int(input())
    powers.append(pi)
powers.sort()
diff = 0
if len(powers) > 1:
    for i in range(1, len(powers)):
        deltas.append(powers[i] - powers[i - 1])
    diff = min(deltas)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(diff)
