import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop

MAX_V_SPEED: int = 40
MAX_THRUST = 4
MAX_X = 3000
V_RATIO = 1.2
X_RATIO = 6
delta_v: int = 0
prev_v_speed: int = 0
prev_thrust: int = 0
thrust: int = 0

while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    delta_v = v_speed - prev_v_speed

    thrust = int(
        prev_thrust +
        V_RATIO * delta_v * (v_speed / MAX_V_SPEED) *
        X_RATIO * ((MAX_X - x) / MAX_X))
    thrust = min(thrust, MAX_THRUST)

    prev_v_speed = v_speed
    prev_thrust = thrust

    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print("0", thrust)
