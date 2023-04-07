# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

# test_hashable = [
#     '13955',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13957',
#     '13957',
#     '13957',
#     '13957',
#     '13957',
#     '13957',
#     '13957',
#     '13957',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '12222',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '14544',
#     '13956',
#     '13957',
#     '13957',
#     '13957',
#     '13957',
#     '13956',
#     '13956',
#     '13956',
#     '13956',
#     '13957',
# ]

# programs = [
#     {
#         'hash_function': 'division',
#         'modulo': 120,
#         'buckets': 1,
#         'collision_scheme': 'linear',
#         'print_width': 5
#     },
#     {
#         'hash_function': 'division',
#         'modulo': 120,
#         'buckets': 1,
#         'collision_scheme': 'quadratic',
#         'print_width': 5
#     },
#     {
#         'hash_function': 'division',
#         'modulo': 120,
#         'buckets': 1,
#         'collision_scheme': 'chain',
#         'print_width': 5
#     },
#     {
#         'hash_function': 'division',
#         'modulo': 113,
#         'buckets': 1,
#         'collision_scheme': 'linear',
#         'print_width': 5
#     },
#     {
#         'hash_function': 'division',
#         'modulo': 113,
#         'buckets': 1,
#         'collision_scheme': 'quadratic',
#         'print_width': 5
#     },
#     {
#         'hash_function': 'division',
#         'modulo': 113,
#         'buckets': 1,
#         'collision_scheme': 'chain',
#         'print_width': 5
#     },
#     {
#         'hash_function': 'division',
#         'modulo': 41,
#         'buckets': 3,
#         'collision_scheme': 'linear',
#         'print_width': 3
#     },
#     {
#         'hash_function': 'division',
#         'modulo': 41,
#         'buckets': 3,
#         'collision_scheme': 'quadratic',
#         'print_width': 3
#     },
# ]

from lib.hashes import hash_by_division, hash_by_multiplication
from lib.input_handler import parse_file
from lib.output_handler import pretty_print_results


def init_table(bucket_size=1, table_size=120, chaining=False):
    if table_size % bucket_size != 0:
        raise IndexError("Table size / bucket size has a remainder. Remainder should be 0")

    table_slots = int(table_size / bucket_size)

    if chaining:
        return [['-1'] for _ in range(0, table_slots)]
    else:
        # https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times
        return [['-1' for _ in range(0, bucket_size)] for _ in range(0, table_slots)]


programs = [
    {
        'hash_function': 'student',
        'modulo': 120,
        'buckets': 1,
        'collision_scheme': 'linear',
        'print_width': 5
    },
    {
        'hash_function': 'student',
        'modulo': 120,
        'buckets': 1,
        'collision_scheme': 'quadratic',
        'print_width': 5
    },
    {
        'hash_function': 'student',
        'modulo': 120,
        'buckets': 1,
        'collision_scheme': 'chain',
        'print_width': 5
    },
    {
        'hash_function': 'division',
        'modulo': 120,
        'buckets': 1,
        'collision_scheme': 'linear',
        'print_width': 5
    },
    {
        'hash_function': 'division',
        'modulo': 120,
        'buckets': 1,
        'collision_scheme': 'quadratic',
        'print_width': 5
    },
    {
        'hash_function': 'division',
        'modulo': 120,
        'buckets': 1,
        'collision_scheme': 'chain',
        'print_width': 5
    }
]


hashables = parse_file("inputs/LabHashingInput.txt")

for hashable in hashables:
    for program in programs:
        table = init_table(program['buckets'], 120, program['collision_scheme'] == 'chain')
        failed = []
        succeeded = []
        agg_stats = []

        for value in hashable:
            if program['hash_function'] == 'student':
                stats = hash_by_multiplication(value, table, program['collision_scheme'], program['buckets'])
            else:
                stats = hash_by_division(value, table, program['modulo'], program['collision_scheme'], program['buckets'])

            agg_stats.append(stats)

            if stats['key'] == -1:
                print(f'Failed to store {value}')
                failed.append(stats)
            else:
                succeeded.append(value)

        pretty_print_results(table, program, agg_stats, succeeded, failed)
