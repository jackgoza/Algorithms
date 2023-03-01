import math

pointss = [[0, 0], [1, 6], [2, 3], [5, 2], [6, 5], [7, 1], [8, 4]]
ppp = [1, 5, 147, 52, 16]
dist = [[], [], [], [], [], []]


def sort(points):
    return sorted(points, key=lambda val: val[0])


def calc_distance(i, j, points):
    if dist[i][j] != 0:
        print(dist[i][j])
        return dist[i][j]

    dist[i][j] = min(calc_distance(i + 1, j, points) + math.dist(points[i], points[i + 1]),
                     calc_distance(i + 1, i, points) + math.dist(points[j], points[i + 1]))

    return dist[i][j]

points = sort(pointss)
for i in range(6):
    for j in range(6):
        dist[i].append(0)

for i in range(6):
    dist[5][i] = math.dist(points[5], points[6]) + math.dist(points[i], points[6])

print(dist)
dist1 = {'dist': math.dist(points[0], points[6]), 'prev': points[0]}
print(calc_distance(0, 0, points))
# dist2 = math.dist(points[0], points[2])
print(dist)
# print(dist2)
