# John Goza
# Lab 1 - Strassen's algorithm
# No re-use or reproduction allowed. All rights retained by John Goza.

"""
TYPE DEFS:

single nested array: List of Lists, not nested more than one level

ingested matrix: {
                'order': String,
                'm1': single nested array,
                'm2': single nested array,
                'error': String,
                'inputs': {
                    'matrix_order_string': String,
                    'first_matrix_string': String,
                    'second_matrix_string': String,
                }
            }
"""

from operator import add, sub
from modules.matrix_parser import parse_matrix_file
from modules.matrix_functions import do_math, partition_matrix, rebuild_rows
from modules.output_handler import output_error, output_success


def multiply_matrix(matrix1, matrix2):
    """
    Implements normal, linear matrix multiplication.
    Each element multiplication is counted. This count is summed and returned as the first item in the return tuple
    so that it can be used for analysis. The multiplied array is also returned as it is required output for the lab.
    :param matrix1: single nested array
    :param matrix2: single nested array
    :return: Tuple(int, single nested array)
    """
    count = 0
    n = len(matrix1)
    resulting_matrix = []

    for i in range(0, n):
        row_result = []

        for j in range(0, n):
            acc = 0

            for k in range(0, n):
                count += 1
                acc += matrix1[i][k] * matrix2[k][j]

            row_result.append(acc)

        resulting_matrix.append(row_result)
    return count, resulting_matrix


def strassen_multiply_matrix(matrix1, matrix2):
    """
    Applies the Strassen algorithm as defined in the book "Introduction to Algorithms Third Edition" (Cormen et. al)
    The algorithm is applied recursively, and each matrix multiplication step is counted. This count is summed and
    returned as the first item in the return tuple so that it can be used for analysis. The multiplied array is also
    returned as it is required output for the lab.
    :param matrix1: single nested array
    :param matrix2: single nested array
    :return: Tuple(int, single nested array)
    """
    if not matrix1 or not matrix2:
        raise Exception

    if len(matrix1) == 1:
        # return a 1 for counting, and the result
        # has to be double wrapped so that [i][j] access does not throw an error
        return 1, [[matrix1[0][0] * matrix2[0][0]]]

    a00, a01, a10, a11 = partition_matrix(matrix1)
    b00, b01, b10, b11 = partition_matrix(matrix2)

    count1, p1 = strassen_multiply_matrix(a00, do_math(sub, b01, b11))
    count2, p2 = strassen_multiply_matrix(do_math(add, a00, a01), b11)
    count3, p3 = strassen_multiply_matrix(do_math(add, a10, a11), b00)
    count4, p4 = strassen_multiply_matrix(a11, do_math(sub, b10, b00))
    count5, p5 = strassen_multiply_matrix(do_math(add, a00, a11), do_math(add, b00, b11))
    count6, p6 = strassen_multiply_matrix(do_math(sub, a01, a11), do_math(add, b10, b11))
    count7, p7 = strassen_multiply_matrix(do_math(sub, a00, a10), do_math(add, b00, b01))

    # Sum the number of multiplications the recursive calls took
    count_total = count1 + count2 + count3 + count4 + count5 + count6 + count7

    c00 = do_math(add, do_math(sub, do_math(add, p5, p4), p2), p6)
    c01 = do_math(add, p1, p2)
    c10 = do_math(add, p3, p4)
    c11 = do_math(sub, do_math(sub, do_math(add, p1, p5), p3), p7)
    return count_total, rebuild_rows(c00, c01) + rebuild_rows(c10, c11)


if __name__ == "__main__":
    runnables = parse_matrix_file("input/input.txt")
    for runnable in runnables:
        if runnable['error'] != '':
            output_error("output/output.txt", runnable)
            continue

        ordinary_result = multiply_matrix(runnable['m1'], runnable['m2'])
        strassen_result = strassen_multiply_matrix(runnable['m1'], runnable['m2'])
        output_success("output/output.txt", ordinary_result, strassen_result, runnable)
