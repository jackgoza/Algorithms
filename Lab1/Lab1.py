# John Goza
# Lab 1 - Strassen's algorithm
import re
from operator import add


# format_matrix(order: int, matrix: flat array)
# takes a flat array of matrix values in row major order and maps them to a nested array
# where each index of the array contains one row of the matrix
def format_matrix(order, matrix):
    formatted_matrix = []
    # God bless python for being a zero-indexed language but dang this is annoying
    for i in range(1, order + 1):
        upper_bound = order * i
        lower_bound = upper_bound - order
        formatted_matrix.append(matrix[lower_bound:upper_bound])
    return formatted_matrix


# validate_input_matrix_constraints(matrix in form of [[a, b],[c, d]])
#   checks that a given matrix is both n x n and that n is an exact power of 2
#   returns: None, throws: Exception if either constraint is not met
def validate_matrix_constraints(input_matrix):
    row_count = len(input_matrix)

    # todo: cite: https://stackoverflow.com/questions/57025836/how-to-check-if-a-given-number-is-a-power-of-two
    if (row_count & (row_count - 1) != 0) or row_count == 0:
        raise Exception("Invalid input given! Matrix is not an exact power of two!")

    for row in input_matrix:
        if len(row) != row_count:
            raise Exception("Invalid input given! Rows and columns differ in length.")


# A file with required input is provided. All input you create should be formatted the same: the
# first line should contain the order of the matrix, then the first matrix, in row major order, then
# the second matrix. This is followed by a blank line, then the order of the next matrix pair and
# so on.
def parse_matrix_file(filename):
    try:
        # todo: cite? https://docs.python.org/3/tutorial/inputoutput.html
        file = open(filename, 'r', encoding='utf-8')
        matrix_order_str = file.readline().strip()
        first_matrix_string = file.readline().strip()
        second_matrix_string = file.readline().strip()

        reg = re.compile(r"(\d*)x(\d*)")
        order_string = reg.search(matrix_order_str).groups()
        if not order_string \
                or order_string[0] != order_string[1] \
                or not order_string[0].isdigit():
            raise Exception(f"Order string is invalid! Given: {matrix_order_str}")

        order = int(order_string[0])

        if (order & (order - 1) != 0):
            raise Exception(f"Order is not an exact power of two! Given: {matrix_order_str}")

        first_flat_matrix = list(map(int, first_matrix_string.split()))
        second_flat_matrix = list(map(int, second_matrix_string.split()))

        first_matrix = format_matrix(order, first_flat_matrix)
        second_matrix = format_matrix(order, second_flat_matrix)

        validate_matrix_constraints(first_matrix)
        validate_matrix_constraints(second_matrix)

        return order, first_matrix, second_matrix
    except Exception as e:
        print("File parsing failed")
        raise e


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


def rebuild_rows(matrix1, matrix2):
    return [row1 + row2 for row1, row2 in zip(matrix1, matrix2)]


# todo: cite https://stackoverflow.com/questions/18713321/element-wise-addition-of-2-lists
def sum_result(matrix1, matrix2):
    sum_matrix = []
    for i in range(len(matrix1)):
        sum_matrix.append(list(map(add, matrix1[i], matrix2[i])))

    return sum_matrix


def recursive_multiply_matrix(matrix1, matrix2):
    if not matrix1:
        raise Exception

    if isinstance(matrix1, int):
        return matrix1 * matrix2
    if len(matrix1) == 1:
        # has to be double wrapped so that [i][j] access does not throw an error
        return [[matrix1[0][0] * matrix2[0][0]]]

    a00, a01, a10, a11 = partition_matrix(matrix1)
    b00, b01, b10, b11 = partition_matrix(matrix2)

    c00 = sum_result(recursive_multiply_matrix(a00, b00), recursive_multiply_matrix(a01, b10))
    c01 = sum_result(recursive_multiply_matrix(a00, b01), recursive_multiply_matrix(a01, b11))
    c10 = sum_result(recursive_multiply_matrix(a10, b00), recursive_multiply_matrix(a11, b10))
    c11 = sum_result(recursive_multiply_matrix(a10, b01), recursive_multiply_matrix(a11, b11))

    print(c00)
    print(c01)
    ans = rebuild_rows(c00, c01) + rebuild_rows(c10, c11)

    return ans


def strassen_multiply_matrix(matrix1, matrix2):
    if not matrix1 or not matrix2:
        raise Exception

    if isinstance(matrix1, int):
        return matrix1 * matrix2
    if len(matrix1) == 1:
        # has to be double wrapped so that [i][j] access does not throw an error
        return [[matrix1[0][0] * matrix2[0][0]]]

    a00, a01, a10, a11 = partition_matrix(matrix1)
    b00, b01, b10, b11 = partition_matrix(matrix2)

    return a00, a01, a10, a11


if __name__ == "__main__":
    # matrix1 = [[2,1], [1,5]]
    # matrix2 = [[6,7], [4,3]]
    # # ans should be [[16, 17], [26, 22]]

    input_matrix_1 = [[1, 1, 11, 11], [2, 2, 22, 22], [3, 3, 33, 33], [4, 4, 44, 44]]
    input_matrix_2 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    # ans should be [[24, 24, 24, 24], [48, 48, 48, 48], [72, 72, 72, 72], [96, 96, 96, 96]]

    print(recursive_multiply_matrix(input_matrix_1, input_matrix_2))
