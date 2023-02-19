# John Goza
# Lab 1 - Strassen's algorithm
# No re-use or reproduction allowed. All rights retained by John Goza.
import json
import re

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


def format_matrix(order, matrix):
    """
    format_matrix takes a flat array of matrix values in row major order and maps them to a nested array
    where each index of the array contains one row of the matrix, and each secondary index is a column in that row.
    e.g. [1 2 3 4] => [[1, 2], [3, 4]]
    :param order: int
    :param matrix: flat array
    :return: single nested array
    """
    formatted_matrix = []
    # God bless python for being a zero-indexed language but dang this is annoying
    for i in range(1, order + 1):
        upper_bound = order * i
        lower_bound = upper_bound - order
        formatted_matrix.append(matrix[lower_bound:upper_bound])
    return formatted_matrix


def validate_matrix_constraints(input_matrix):
    """
    Checks that a given matrix is both n x n and that n is an exact power of 2
    :param input_matrix: single nested array
    :return: None
    :throws Exception if constraints are not met
    """
    row_count = len(input_matrix)

    # todo: cite: https://stackoverflow.com/questions/57025836/how-to-check-if-a-given-number-is-a-power-of-two
    if (row_count & (row_count - 1) != 0) or row_count == 0:
        raise Exception("Invalid input given! Matrix is not an exact power of two!")

    # Validate row length == column length for all columns
    for row in input_matrix:
        if len(row) != row_count:
            raise Exception("Invalid input given! Rows and columns differ in length.")


# TODO: comment this method
def ingest_single_input(matrix_order, first_matrix_string, second_matrix_string):
    """
    Parses, transforms and validates a single three line section of the input file.
    Catches exceptions raised during parsing and places them as a String on the returned object.
    This prevents consuming methods from needing try / except logic.
    :param matrix_order_str: String
    :param first_matrix_string: String
    :param second_matrix_string: String
    :return: ingested matrix
    """
    try:
        if (matrix_order & (matrix_order - 1) != 0):
            raise Exception(f"Order is not an exact power of two! Given: {matrix_order}")

        first_flat_matrix = list(map(int, first_matrix_string.split()))
        second_flat_matrix = list(map(int, second_matrix_string.split()))

        first_matrix = format_matrix(matrix_order, first_flat_matrix)
        second_matrix = format_matrix(matrix_order, second_flat_matrix)

        validate_matrix_constraints(first_matrix)
        validate_matrix_constraints(second_matrix)

        return {'order': matrix_order, 'm1': first_matrix, 'm2': second_matrix, 'error': '',
                'inputs': {'matrix_order_str': matrix_order,
                           'first_matrix_string': first_matrix_string,
                           'second_matrix_string': second_matrix_string}}
    except Exception as e:
        return {'error': repr(e), 'inputs': {'matrix_order_str': matrix_order,
                                             'first_matrix_string': first_matrix_string,
                                             'second_matrix_string': second_matrix_string}}


def parse_matrix_file(filename):
    """
    Opens file for reading and splits into sets of 3. Those sets are mapped into an array of ingested matrix objects
    via the ingest_single_input function. The mapped array is then returned. Errors other than IO will be returned as
    a string on the specific object that had an error, thus valid order matrix matrix sets will still be processed.
    :param filename: String
    :return: List(ingested matrix)
    :throws: Exception if file IO fails
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file_in:
            inputs = []

            order = 0
            matrix = []

            while line := file_in.readline():
                # first line should be the matrix order
                # we are going to ignore lines beginning with '#' so that I can put comments in the test file

                # if there are no matrix elements or an order string on a line
                if line == '\n':
                    # if we're currently ingesting a matrix
                    if order != 0:
                        processed = ingest_single_input(order, ' '.join(matrix[:order]), ' '.join(matrix[order:]))
                        inputs.append(processed)
                        order = 0
                        matrix = []

                    # go to next line
                    continue

                # if we are not currently ingesting a matrix
                if order == 0:
                    # set the order
                    order = int(line.strip())
                    # go to next line
                    continue

                # add matrix element to current ingestion
                matrix.append(line.strip().replace("  ", " "))

            return inputs

    except Exception as e:
        print(f"File parsing failed: {repr(e)}")
        raise e
