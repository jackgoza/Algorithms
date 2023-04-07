# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

from os import path


def get_printable(key, table):
    if table[key][0] == '-1':
        return ' XXXXXXX '
    else:
        return str(table[key])


def pretty_print_results(table, program, stats, succeeded, failed):
    print_width = program['print_width']
    print(f"Method: {program['hash_function']}, mod: {program['modulo']}")
    print(f"Bucket size: {program['buckets']}")
    print(f"Collision handling: {program['collision_scheme']}")
    print('')

    for i in range(0, len(table), print_width):
        printables = []
        for j in range(0, print_width):
            printables.append(get_printable(i + j, table))

        print(f"Bucket {i + 1: <3}-{i + print_width:>3}{':': <6}{' '.join(printables)}")

    print('')