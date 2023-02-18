# John Goza
# Lab 1 - Strassen's algorithm
# No re-use or reproduction allowed. All rights retained by John Goza.

# partition_matrix(matrix: single nested array)
# returns quadrants[0], quadrants[1], quadrants[2], quadrants[3]: all single nested arrays
# takes an n x n matrix and splits it into four quadrants.
# e.g. [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]] would return
#      [[1, 1], [2, 2]]      [[1, 1], [2, 2]]     [[3, 3], [4, 4]]     [[3, 3], [4, 4]]
def partition_matrix(matrix):
    quadrants = [[], [], [], []]

    half_len = int(len(matrix) / 2)
    for i in range(0, len(matrix)):
        if i < half_len:
            quadrants[0].append(matrix[i][0:half_len])
            quadrants[1].append(matrix[i][half_len:])
        else:
            quadrants[2].append(matrix[i][0:half_len])
            quadrants[3].append(matrix[i][half_len:])

    return quadrants[0], quadrants[1], quadrants[2], quadrants[3]


# rebuild_rows(matrix1: single nested array, matrix2: single nested array)
# returns single nested matrix with each row in matrix2 appended to its corresponding row in matrix1
# e.g. given matrix1=[[72, 72], [96, 96]], matrix2=[[72, 72], [96, 96]], it outputs [[72, 72, 72, 72], [96, 96, 96, 96]]
def rebuild_rows(matrix1, matrix2):
    return [row1 + row2 for row1, row2 in zip(matrix1, matrix2)]


# def do_math(operand: Python operator, matrix1: single nested array, matrix2: single nested array)
# returns resulting_matrix: single nested array
# applies the supplied math operator (add, sub) element by element across the two input matrices
# e.g. given operand=add, matrix1=[[5, 7], [1, 2]], matrix2=[[3, 4], [8, 13]], it outputs [[8, 11], [9, 15]]
# e.g. given operand=sub, matrix1=[[5, 7], [1, 2]], matrix2=[[3, 4], [8, 13]], it outputs [[2, 3], [-7, -11]]
# todo: cite https://stackoverflow.com/questions/18713321/element-wise-addition-of-2-lists
def do_math(operand, matrix1, matrix2):
    resulting_matrix = []
    for i in range(len(matrix1)):
        resulting_matrix.append(list(map(operand, matrix1[i], matrix2[i])))

    return resulting_matrix

