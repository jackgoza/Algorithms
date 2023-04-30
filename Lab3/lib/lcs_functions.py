# John Goza
# Lab 3 - Dynamic
# No re-use or reproduction allowed. All rights retained by John Goza.


def init_tables(m, n):
    b = [['-1' for _ in range(0, n)] for _ in range(0, m)]
    c = [[None for _ in range(0, n + 1)] for _ in range(0, m + 1)]
    return b, c


def generate_lcs_table(x, y):
    m = len(x)
    n = len(y)
    b, c = init_tables(m, n)

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c


def walk_lcs_path(matrix, x, y, i, j, curr=''):
    if i == 0 or j == 0:
        return curr

    if x[i-1] == y[j-1]:
        new_curr = walk_lcs_path(matrix, x, y, i - 1, j - 1, curr)
        return new_curr + x[i - 1]
    elif matrix[i - 1][j] >= matrix[i][j - 1]:
        return walk_lcs_path(matrix, x, y, i - 1, j, curr)
    else:
        return walk_lcs_path(matrix, x, y, i, j - 1, curr)
