import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

temp_negative = False
temp_closest = math.inf

n = int(input())  # the number of temperatures to analyse

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    t_abs = abs(t)
    temp_closest_abs = abs(temp_closest)
    if t_abs < temp_closest_abs:
        temp_closest = t
        if t < 0:
            temp_negative = True
    if t_abs == temp_closest_abs and t > 0:
        temp_closest = t
        temp_negative = False

if temp_closest == math.inf:
    temp_closest = 0
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(temp_closest)
