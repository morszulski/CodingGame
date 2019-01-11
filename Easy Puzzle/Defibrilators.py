import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())

dist = float('inf')
name = None
lon = float(lon.replace(',', '.')) * math.pi / 180
lat = float(lat.replace(',', '.')) * math.pi / 180

for i in range(n):
    defib = input()
    d_num, d_name, d_address, d_phone, d_lon, d_lat, *_ = defib.split(';')
    d_lon = float(d_lon.replace(',', '.')) * math.pi / 180
    d_lat = float(d_lat.replace(',', '.')) * math.pi / 180
    x = (d_lon - lon) * math.cos((d_lat + lat) / 2)
    y = (d_lat - lat)
    d = math.sqrt(x * x + y * y) * 6371
    if d < dist:
        dist = d
        name = d_name
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(name)
