# John Goza
# Lab 3 - Dynamic
# No re-use or reproduction allowed. All rights retained by John Goza.

import copy

# https://stackoverflow.com/questions/13214809/pretty-print-2d-list/50257693#50257693
def pretty_print_matrix(matrix, x, y):
    combined_matrix = copy.deepcopy(matrix)
    x[0:0] = [' ']
    y[0:0] = [' ', ' ']
    [row.insert(0, x[i]) for i, row in enumerate(combined_matrix)]
    combined_matrix.insert(0, y)
    print('\n'.join(['   '.join([str(cell) for cell in row]) for row in combined_matrix]))

