# John Goza
# Lab 3 - Dynamic
# No re-use or reproduction allowed. All rights retained by John Goza.
import argparse
import itertools

from lib.input_handler import parse_file
from lib.lcs_functions import generate_lcs_table, walk_lcs_path
from lib.output_handler import OutputHandler

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input-file', default="", required=False)
    arg_parser.add_argument('--console', default=False, required=False, nargs='?', const=True)
    arg_parser.add_argument('--quiet', default=False, required=False, nargs='?', const=True)
    arg_parser.add_argument('--output-file', default="outputs/output.txt", required=False)
    arg_parser.add_argument('--test', default=False, required=False, nargs='?', const=True)
    args = vars(arg_parser.parse_args())

    input_file = args["input_file"]
    output_to_console = args['console'] or args['console'] == "true"
    output_file = args["output_file"]
    run_tests = args['test'] or args['test'] == "true"
    quiet = args['quiet'] or args['quiet'] == "true"
    show_details = not quiet
    default_input = 'inputs/DynamicLabInput.txt' if not run_tests else 'inputs/TestInput.txt'
    method = "combo" if output_to_console else 'file'

    runnables = parse_file(default_input) if input_file == "" else parse_file(input_file)

    outputter = OutputHandler(show_details=show_details, method=method, filename=output_file)
    outputter.print_parsed(runnables)

    combo = list(itertools.combinations(runnables.items(), 2))

    for pair in combo:
        x = pair[0][1]
        y = pair[1][1]
        matrix, table_count, honest_count = generate_lcs_table(x, y)

        lcs, walk_count = walk_lcs_path(matrix, x, y, len(matrix) - 1, len(matrix[0]) - 1, 0)

        outputter.print_output(lcs, matrix, x, y, pair[0][0], pair[1][0], table_count, honest_count, walk_count)
