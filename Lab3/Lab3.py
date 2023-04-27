# John Goza
# Lab 3 - Dynamic
# No re-use or reproduction allowed. All rights retained by John Goza.
import argparse


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


# https://stackoverflow.com/questions/13214809/pretty-print-2d-list/50257693#50257693
def pretty_print_matrix(matrix):
    print('\n'.join(['   '.join([str(cell) for cell in row]) for row in matrix]))


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input-file', default="inputs/DynamicLabInput.txt", required=False)
    arg_parser.add_argument('--console', default=False, required=False, nargs='?', const=True)
    arg_parser.add_argument('--output-file', default="outputs/output.txt", required=False)
    arg_parser.add_argument('--report', default=False, required=False, nargs='?', const=True)
    arg_parser.add_argument('--report-file', default="outputs/report.csv", required=False)
    arg_parser.add_argument('--test', default=False, required=False, nargs='?', const=True)
    args = vars(arg_parser.parse_args())

    input_file = args["input_file"]
    output_to_console = args['console'] or args['console'] == "true"
    output_file = args["output_file"]
    make_report = args['report'] or args['report'] == "true"
    report_file = args["report_file"]
    run_tests = args['test'] or args['test'] == "true"
    x = "ABCBDAB"
    y = "BDCABA"
    matrix = generate_lcs_table(x, y)
    pretty_print_matrix(matrix)
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    print(walk_lcs_path(matrix, x, y, i, j))
