# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.


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

from lib.hashes import hash_by_division
from lib.output_handler import pretty_print_results


def init_table(bucket_size=1, table_size=120):
    if table_size % bucket_size != 0:
        raise IndexError("Table size / bucket size has a remainder. Remainder should be 0")

    table_slots = int(table_size / bucket_size)

    # https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times
    return [[None, '-1'] for _ in range(0, table_slots)]
    # return [[None, ['-1'] * bucket_size]] * table_slots


def init_stack(table_size=120):
    return list(range(table_size))

programs = [
    {
        'hash_function': 'division',
        'modulo': 120,
        'buckets': 1,
        'collision_scheme': 'linear',
        'print_width': 5
    },
]


test_hashable = [
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
    '13956',
]

# hashables = parse_file("inputs/LabHashingInput.txt")
hashables = [test_hashable]
for hashable in hashables:
    for program in programs:
        table = init_table(program['buckets'], 120)

        if program['collision_scheme'] == 'chain':
            stack = init_stack()

        for value in hashable:
            print(value)
            stats = hash_by_division(value, table, program['modulo'], program['collision_scheme'])
            print(stats)

        pretty_print_results(table)

# for i in test_input:
# 	val = hash_by_division(i, init_table)
# 	print(f"{i}, {val}")
#
# pretty_print_results(init_table)
