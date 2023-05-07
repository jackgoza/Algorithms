# John Goza
# Lab 3 - Dynamic
# No re-use or reproduction allowed. All rights retained by John Goza.

import copy


class OutputHandler:
    def __init__(self, show_details=True, method='', filename='output.txt'):
        self.show_details = show_details
        self.method = method
        self.filename = filename
        if method == 'file' or method == 'combo':
            self.file = open(filename, "w")

    def write_out(self, string):
        if self.method == 'file':
            self.file.write(string)
        elif self.method == 'combo':
            print(string)
            self.file.write(string + '\n')
        else:
            print(string)

    def print_parsed(self, sequences):
        self.write_out(f'Number of sequences to be compared: {len(sequences)}')
        self.write_out('')
        for item in sequences.items():
            self.write_out(f'Sequence {item[0]} | Length: {len(item[1])}')
            self.write_out(' '.join(item[1]))
            self.write_out('')

    def print_header(self, title1, title2, lcs, x_len, y_len, table_count, honest_count, walk_count):
        if self.show_details:
            self.write_out(f'Comparing sequences {title1} and {title2}')
            self.write_out(f'Iterations to build: {table_count} | Comparisons to build: {honest_count} | Comparisons to walk: {walk_count}')
            self.write_out(f'{title1} length: {x_len} | {title2} length: {y_len} | LCS Length: {len(lcs)}')
            self.write_out(f'{" ".join(lcs)}')
            self.write_out('')
        else:
            self.write_out(f'{title1}, {title2}, {x_len}, {y_len}, {x_len * y_len}, {table_count}, {honest_count}, {x_len + y_len}, {walk_count}')

    def pretty_print_matrix(self, matrix, x, y):
        # https://stackoverflow.com/questions/13214809/pretty-print-2d-list/50257693#50257693
        combined_matrix = copy.deepcopy(matrix)
        x[0:0] = [' ']
        y[0:0] = [' ', ' ']
        [row.insert(0, x[i]) for i, row in enumerate(combined_matrix)]
        combined_matrix.insert(0, y)
        self.write_out('\n'.join(['   '.join([str(cell) for cell in row]) for row in combined_matrix]))
        self.write_out('\n\n')

    def print_output(self, lcs, matrix, x, y, title1, title2, table_count, honest_count, walk_count):
        self.print_header(title1, title2, lcs, len(x), len(y), table_count, honest_count, walk_count)
        if self.show_details:
            # The list(var)[:] constructs here are required due to Python trying to pass this by reference :(
            # We are essentially doing a cheap "deep copy"
            self.pretty_print_matrix(matrix, list(x)[:], list(y)[:])
