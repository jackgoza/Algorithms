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


def delete_old_report_file(filename):
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except IOError as ioe:
            print('Unable to delete old report file; see error below.')
            print('Old report file may be appended to as program continues. It is recommended that you')
            print('delete the file after program is done.')
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


def get_printable(key, table, bucket_size):
    if table[key][0] == '-1':
        return ' XXXXXXX ' if bucket_size == 1 else ' ------- '
    else:
        return str(table[key])


def pretty_print_results(table, program, stats, succeeded, failed):
    agg_stats = aggregate_stats(stats)
    print_width = program['print_width']
    bucket_size = program['buckets']
    print(f"Method: {program['hash_function']}, Mod: {program['modulo']}")
    print(f"Bucket size: {bucket_size}, Bucket count: {int(120 / int(program['buckets']))}")
    print(f"Collision handling: {program['collision_scheme']}")
    print(f"Number of comparisons: {agg_stats['comparisons']}")
    print(
        f"Number of collisions - Primary: {agg_stats['primary_collisions']}, Secondary: {agg_stats['secondary_collisions']}")
    print(f"Number of items not inserted: {len(failed)}")
    print(f"Load factor: {round(len(succeeded) / 120, 2)}")

    table_len = len(table)

    for i in range(0, len(table), print_width):
        printables = []
        for j in range(0, print_width):

            # Catch those situations where (120 / buckets) % print_width != 0
            if i + j >= table_len:
                continue
            try:
                printables.append(get_printable(i + j, table, bucket_size))
            except IndexError as e:
                print("OH NO")
                continue

        print(f"Bucket {i + 1: <3}-{i + print_width:>3}{':': <6}{' '.join(printables)}")

    print('')
