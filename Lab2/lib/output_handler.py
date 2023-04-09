# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

import os


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


def delete_old_file(filename):
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except IOError as ioe:
            print('Unable to delete old file; see error below.')
            print('Old file may be appended to as program continues. It is recommended that you')
            print('manually delete the file after program is done.')
            print(ioe)


def write_line(filename, line):
    try:
        file = open(filename, 'a')
        file.write(line + '\n')
        file.close()
    except IOError as ioe:
        print('Unable to write line! Proceeding with program.')
        print(ioe)


def write_report_line(filename, program, stats, succeeded, failed):
    agg_stats = aggregate_stats(stats)

    line = " ".join([
        f"{program['hash_function']}, {program['modulo']}, {program['buckets']},",
        f"{int(120 / int(program['buckets']))}, {program['collision_scheme']},",
        f"{agg_stats['comparisons']}, {agg_stats['primary_collisions']},",
        f"{agg_stats['secondary_collisions']}, {len(failed)}, {round(len(succeeded) / 120, 2)}"
    ])
    write_line(filename, line)


def get_printable(i, j, table, bucket_size, is_chained):
    if bucket_size > 1:
        x = i
        y = j
    else:
        x = i + j
        y = 0

    if is_chained and len(table[x]) > 1:
        return f'{len(table[x])} items'
    elif table[x][y] == '-1':
        return ' ----- '
    else:
        return ' ' + table[x][y] + ' '


def pretty_print_results(table, program, stats, succeeded, failed, output_to_console, output_file):
    agg_stats = aggregate_stats(stats)
    print_width = program['print_width']
    bucket_size = program['buckets']
    is_chained = program['collision_scheme'] == 'chain'
    output_lines = [
        f"Method: {program['hash_function']}, Mod: {program['modulo']}",
        f"Bucket size: {bucket_size}, Bucket count: {int(120 / int(program['buckets']))}",
        f"Collision handling: {program['collision_scheme']}",
        f"Number of comparisons: {agg_stats['comparisons']}",
        f"Number of collisions - Primary: {agg_stats['primary_collisions']}, Secondary: {agg_stats['secondary_collisions']}",
        f"Number of items not inserted: {len(failed)}",
        f"Load factor: {round(len(succeeded) / 120, 2)}",
    ]

    i_increment = 1 if bucket_size > 1 else print_width
    j_max = bucket_size if bucket_size > 1 else print_width

    for i in range(0, len(table), i_increment):
        printables = []
        for j in range(0, j_max):
            printables.append(get_printable(i, j, table, bucket_size, is_chained))

        if bucket_size > 1:
            output_lines.append(f"{i + 1: <3}{':': <6}{' '.join(printables)}")
        else:
            output_lines.append(f"{i + 1: <3}-{i + print_width:>3}{':': <6}{' '.join(printables)}")

    if output_to_console:
        [print(line) for line in output_lines]
        print('\n')
    else:
        [write_line(output_file, line) for line in output_lines]
        write_line(output_file, '\n')
