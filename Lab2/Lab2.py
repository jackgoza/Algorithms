# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

"""
TYPE DEFS:

config:
    {
        'hash_function': String('division'|'student'),
        'modulo': Integer,
        'buckets': Integer,
        'collision_scheme': String('linear'|'quadratic'|'chain'),
        'print_width': Integer,
        'c1': Optional Float,
        'c2': Optional Float
    }

formatted_result:
    {
        'key': Integer,
        'value': String,
        'collisions': Array[Integer],
        'comparisons': Integer
    }

hash_table:
        Array[ Array[ String ] ]

        Strings are defaulted to '-1'
"""

import argparse

from config import standard_configs, test_configs
from lib.hasher import hash_values
from lib.input_handler import parse_file
from lib.output_handler import pretty_print_results, write_line, write_report_line, delete_old_file


def init_table(program):
    """
    Initializes a hash_table array for the given config's bucket size and collision scheme.

    If buckets == 1, hash_table will be [['-1'], ['-1'], ..., ['-1']]

    If buckets == 2, hash_table will be [['-1', '-1'], ['-1', '-1'], ..., ['-1', '-1']]

    Pattern persists as buckets increases
    :param program: config
    :return: hash_table
    """
    bucket_size = program['buckets']
    table_size = 120

    if table_size % bucket_size != 0:
        raise IndexError("Table size / bucket size has a remainder. Remainder should be 0")

    table_slots = int(table_size / bucket_size)

    if program['collision_scheme'] == 'chain':
        return [['-1'] for _ in range(0, table_slots)]
    else:
        # https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times
        return [['-1' for _ in range(0, bucket_size)] for _ in range(0, table_slots)]


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input-file', default="inputs/LabHashingInput.txt", required=False)
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

    if make_report:
        delete_old_file(report_file)
        header = " ".join([
            "Hashing Function, Modulo, Bucket Size, Bucket Count, Collision Handling, Comparisons,",
            "Primary Collisions, Secondary Collisions, Failed Inserts, Load Factor"
        ])
        write_line(report_file, header)

    if not output_to_console:
        delete_old_file(output_file)

    if run_tests:
        if input_file == "inputs/LabHashingInput.txt":
            raise Exception("--input-file must be set if using the --test flag!")
        else:
            hashables = parse_file(input_file)
            programs = test_configs
    else:
        hashables = parse_file(input_file)
        configs = standard_configs

    for hashable in hashables:
        for config in configs:
            table = init_table(config)

            agg_stats, failed, succeeded = hash_values(config, hashable, table)

            if make_report:
                write_report_line(report_file, config, agg_stats, succeeded, failed)

            pretty_print_results(table, config, agg_stats, succeeded, failed, output_to_console, output_file)
