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


def pretty_print_original_matrix(order, matrix_string):
    elements = matrix_string.split(' ')
    matrix = ''
    row = ''
    if len(elements) > order ** 2:
        return matrix_string
    try:
        for i in range(order):
            for j in range(order):
                element = elements[i * order + j]
                if element[0] == "-":
                    row += f" {element} "
                else:
                    row += f"  {element} "
            matrix += row + '\n'
            row = ''
        return matrix
    except IndexError:
        return matrix + '\n' + matrix_string


def pretty_print_result_matrix(order, matrix):
    matrix_string = ''
    row = ''
    for i in range(order):
        for j in range(order):
            element = matrix[i][j]
            if element < -99:
                row += f"{element} "
            elif element < -9:
                row += f" {element} "
            elif element < 0:
                row += f"  {element} "
            elif element > 99:
                row += f" {element} "
            elif element > 9:
                row += f"  {element} "
            else:
                row += f"   {element} "
        matrix_string += row + '\n'
        row = ''
    return matrix_string


def output_error(filename, runnable):
    try:
        with open(filename, 'a') as file:
            order = int(runnable['inputs']['matrix_order_str'])
            file.write("Unable to multiply matrices for input:")
            file.write('\n')
            file.write(f"{runnable['inputs']['matrix_order_str']}\n")
            file.write(pretty_print_original_matrix(order, runnable['inputs']['first_matrix_string']))
            file.write('\n')
            file.write(pretty_print_original_matrix(order, runnable['inputs']['second_matrix_string']))
            file.write('\n')
            file.write('Reason:\n')
            file.write(runnable['error'])
            file.write('\n')
            file.write('\n')
            file.write('\n')
            file.write('\n')
    except Exception as e:
        print(f"Encountered error writing error output to file {filename}")
        print(repr(e))


def output_success(show_resultants, filename, ordinary_result, strassen_result, runnable):
    try:
        with open(filename, 'a') as file:
            order = int(runnable['inputs']['matrix_order_str'])
            file.write(f"Successfully multiplied input of order {order}:\n")
            file.write(f'Ordinary multiplication took {ordinary_result[0]} element multiplications.\n')
            file.write(f'Strassen multiplication took {strassen_result[0]} element multiplications. \n')
            file.write('\n')
            file.write('Matrix inputs were:\n')
            file.write('\n')
            file.write(pretty_print_original_matrix(order, runnable['inputs']['first_matrix_string']))
            file.write('\n')
            file.write(pretty_print_original_matrix(order, runnable['inputs']['second_matrix_string']))
            file.write('\n')
            if show_resultants or show_resultants == 'true':
                file.write("Ordinary multiplication resulting matrix: \n")
                file.write('\n')
                file.write(pretty_print_result_matrix(order, ordinary_result[1]))
                file.write('\n')
                file.write('\n')
                file.write("Strassen multiplication resulting matrix: \n")
                file.write('\n')
                file.write(pretty_print_result_matrix(order, ordinary_result[1]))
                file.write('\n')
                file.write('\n')
                file.write('\n')


    except Exception as e:
        print(f"Encountered error writing success output to file {filename}")
        print(repr(e))
