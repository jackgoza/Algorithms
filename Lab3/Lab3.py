# John Goza
# Lab 3 - Dynamic
# No re-use or reproduction allowed. All rights retained by John Goza.
import argparse

from lib.lcs_functions import generate_lcs_table, walk_lcs_path
from lib.output_handler import pretty_print_matrix

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
    # x = "ABCBDAB"
    # y = "BDCABA"
    x = "ACCGGTCGACTGCGCGGAAGCCGGCCGAA"
    y = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
    matrix = generate_lcs_table(x, y)
    pretty_print_matrix(matrix, list(x)[:], list(y)[:])
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    print(walk_lcs_path(matrix, x, i, j))
