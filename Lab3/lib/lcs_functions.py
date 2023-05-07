# John Goza
# Lab 3 - Dynamic
# No re-use or reproduction allowed. All rights retained by John Goza.


def init_tables(m, n):
    """
    Creates a table/matrix of size MxN.
    :param m: Integer
    :param n: Integer
    :return: [[None, None, ...]]
    """
    c = [[None for _ in range(0, n + 1)] for _ in range(0, m + 1)]
    return c


def generate_lcs_table(x, y):
    """
    Generates the LCS cost matrix for two given strings in a bottom up fashion
    :param x: String
    :param y: String
    :return: [[ Int, Int, Int, ...], []...] table, Integer count, Integer honest_count
    """
    m = len(x)
    n = len(y)
    count = 0
    honest_count = 0
    c = init_tables(m, n)

    for i in range(m + 1):
        for j in range(n + 1):
            count += 1
            if i == 0 or j == 0:
                c[i][j] = 0
                honest_count += 1
            elif x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                honest_count += 2
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
                honest_count += 3

    return c, count, honest_count


def walk_lcs_path(matrix, x, y, i, j, count, curr=''):
    """
    Recursively generates the LCS for a given set of strings and their associated cost matrix
    :param matrix: Cost matrix in form of nested arrays,
    :param x: String,
    :param y: String,
    :param i: Integer, current index
    :param j: Integer, current index
    :param count: Integer, current comparisons
    :param curr: String, current LCS
    :return: String LCS, Integer count
    """
    if i == 0 or j == 0:
        return curr, count

    if x[i-1] == y[j-1]:
        count += 1
        new_curr, new_count = walk_lcs_path(matrix, x, y, i - 1, j - 1, count, curr)
        pos = new_curr + x[i - 1]
        return pos, new_count
    elif matrix[i - 1][j] >= matrix[i][j - 1]:
        count += 2
        return walk_lcs_path(matrix, x, y, i - 1, j, count, curr)
    else:
        count += 2
        return walk_lcs_path(matrix, x, y, i, j - 1, count, curr)
