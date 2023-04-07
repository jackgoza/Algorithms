# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

from os import path


def aggregate_stats(list_of_stats):
    primary_collisions = 0
    secondary_collisions = 0
    total_comparisons = 0
    for i in list_of_stats:
        total_comparisons += i['comparisons']

        if len(i['collisions']) > 0:
            primary_collisions += 1
            secondary_collisions += len(i['collisions']) - 1

    return {'comparisons': total_comparisons, 'primary_collisions': primary_collisions,
            'secondary_collisions': secondary_collisions}


def get_printable(key, table):
    if table[key][0] == '-1':
        return ' XXXXXXX '
    else:
        return str(table[key])


def pretty_print_results(table, program, stats, succeeded, failed):
    agg_stats = aggregate_stats(stats)
    print_width = program['print_width']
    print(f"Method: {program['hash_function']}, Mod: {program['modulo']}")
    print(f"Bucket size: {program['buckets']}, Bucket count: {int(120 / int(program['buckets']))}")
    print(f"Collision handling: {program['collision_scheme']}")
    print(f"Number of comparisons: {agg_stats['comparisons']}")
    print(f"Number of collisions - Primary: {agg_stats['primary_collisions']}, Secondary: {agg_stats['secondary_collisions']}")
    print(f"Number of items not inserted: {len(failed)}")
    print(f"Load factor: {round(len(succeeded) / 120, 2)}")

    for i in range(0, len(table), print_width):
        printables = []
        for j in range(0, print_width):
            printables.append(get_printable(i + j, table))

        print(f"Bucket {i + 1: <3}-{i + print_width:>3}{':': <6}{' '.join(printables)}")

    print('')
