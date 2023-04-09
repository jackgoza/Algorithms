

import math

points = [[0, 6], [1, 0], [2, 3], [5, 4], [6, 1], [7, 5], [8, 2]]


# Function to calculate distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


# Function to calculate the shortest bitonic path
def shortest_bitonic_path(points):
    # Sort points by x-coordinate
    points = sorted(points, key=lambda x: x[0])

    # Initialize variables
    n = len(points)
    dp = [[["", 0] for x in range(n)] for x in range(n)]
    # Compute DP matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j][0] = "diag"
                dp[i][j][1] = 0
                continue
            elif i == 0:
                dp[i][j][0] = 'right'
            elif j == 0:
                dp[i][j][0] = 'right'
            else:
                if i < j:
                    dp[i][j][0] = 'right'
                else:
                    dp[i][j][0] = 'left'
            dp[i][j][1] = distance(points[i], points[j])

    print(dp[0])
    print(dp[1])
    print(dp[2])
    print(dp[3])
    print(dp[4])
    print(dp[5])
    print(dp[6])

    path = [0]
    path_length = 0
    # Compute shortest path from the left most to right most only traveling left to right
    next = 0
    while next != n-1:
        options = dp[next]
        indecies = []
        dist = []
        for option in range(len(options)):
            if options[option][0] == 'right':
                indecies.append(option)
                dist.append(options[option][1])
        next = indecies[dist.index(min(dist))]
        path_length += min(dist)
        path.append(next)

    while len(path) != len(options):
        options = dp[next]
        indecies = []
        dist = []
        for option in range(len(options)):
            if options[option][0] == 'left' and option not in path:
                indecies.append(option)
                dist.append(options[option][1])
        next = indecies[dist.index(min(dist))]
        path_length += min(dist)
        path.append(next)
    path_length += dp[path[0]][path[-1]][1]

    return path, path_length



# Compute shortest bitonic path
path, path_length = shortest_bitonic_path(points)

# Print results
print("Shortest Bitonic Path:", list(map(lambda point: points[point], path)))
print("Length:", path_length)