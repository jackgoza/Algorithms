import math
import numpy as np
import pandas as pd

pointss = [[0, 0], [1, 6], [2, 3], [5, 2], [6, 5], [7, 1], [8, 4]]
dist = pd.DataFrame(np.zeros((7, 7)), index=range(0, 7), columns=range(0, 7))
count = 0


def sort(points):
    return sorted(points, key=lambda val: val[0])


def calc_distance(i, j, points):
    global count
    count = count + 1
    if dist.at[i, j] != 0:
        return dist.at[i, j]

    dist.at[i, j] = round(min(calc_distance(i + 1, j, points) + math.dist(points[i], points[i + 1]),
                              calc_distance(i + 1, i, points) + math.dist(points[j], points[i + 1])), 2)

    print(f"i: {i}, j: {j}, dist: {dist.at[i, j]}")

    return dist.at[i, j]


points = sort(pointss)

for i in range(6):
    dist.at[5, i] = round(math.dist(points[5], points[6]) + math.dist(points[i], points[6]), 2)

count = 0
print(points)
print(calc_distance(0, 0, points))
print(dist)