import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

points = list()

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    points.append((x, y))


class Travel:

    def __init__(self, points: list, start_index=0):
        self.start_index = start_index
        self.start_point = points[self.start_index]
        self.points = points
        self.distance: float = 0.0

    def calculate_distance(
            self,
    ):
        if len(self.points) > 1:
            (x, y) = self.points[self.start_index]
            self.points = self.points[:self.start_index] + self.points[self.start_index + 1:]
            distances = [math.sqrt((x - xi) ** 2 + (y - yi) ** 2) for (xi, yi) in self.points]
            min_distance = min(distances)
            self.distance += min_distance
            self.start_index = distances.index(min_distance)
            return self.calculate_distance()
        else:
            (xi, yi) = self.start_point
            (x, y) = self.points[self.start_index]
            self.distance += math.sqrt((x - xi) ** 2 + (y - yi) ** 2)
            return self.distance


print(round(Travel(points).calculate_distance()))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
