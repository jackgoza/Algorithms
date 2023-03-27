# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

from os import path


def get_printable(key, table):
    if table[key] == '-1':
        return 'XXXXX'
    else:
        return table[key]


def pretty_print_results(table):
    for i in range(0, len(table), 5):
        p1 = get_printable(i, table)
        p2 = get_printable(i + 1, table)
        p3 = get_printable(i + 2, table)
        p4 = get_printable(i + 3, table)
        p5 = get_printable(i + 4, table)
        print(f"Bucket {i + 1}-{i + 5}:    {p1} {p2} {p3} {p4} {p5}")