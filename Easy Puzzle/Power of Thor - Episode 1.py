import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

MAX_X = 39
MAX_Y = 17
MIN_Y = 0
MIN_X = 0

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
ty = initial_ty
tx = initial_tx
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    delta_x = light_x - tx
    delta_y = light_y - ty

    direction_u_d: str = ''
    direction_l_r: str = ''

    if delta_x > 0 and tx == MAX_X:
        delta_x = 0

    if delta_x < 0 and tx == MIN_X:
        delta_x = 0

    if delta_y > 0 and ty == MAX_Y:
        delta_y = 0

    if delta_y < 0 and ty == MIN_Y:
        delta_y = 0

    if delta_y > 0:
        direction_u_d = 'S'
        ty += 1

    if delta_y < 0:
        direction_u_d = 'N'
        ty -= 1

    if delta_x > 0:
        direction_l_r = 'E'
        tx += 1

    if delta_x < 0:
        direction_l_r = 'W'
        tx -= 1

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(f'{direction_u_d}{direction_l_r}')
