# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

"""
TYPE DEFS:
    Reference Lab2.py for information on parameter / object structures
"""

from math import floor, log

from lib.collision_handlers import probe

# CONSTANTS:
# from p264 of Cormen
a_value = 0.618034
log_of_2 = log(2)


def format_result(key, value, collisions, comparisons):
    """

    :param key: Integer
    :param value: String
    :param collisions: Array[Integer]
    :param comparisons: Integer
    :return: formatted_result
    """
    return {
        'key': key,
        'value': value,
        'collisions': collisions,
        'comparisons': comparisons
    }


def hash_values(config, hashable, table):
    agg_stats = []
    failed = []
    succeeded = []

    for value in hashable:
        if config['hash_function'] == 'student':
            stats = hash_by_multiplication(value, table, config['collision_scheme'], config['buckets'])
        else:
            stats = hash_by_division(value, table, config['modulo'], config['collision_scheme'],
                                     config['buckets'])

        agg_stats.append(stats)

        if stats['key'] == -1:
            print(f'Failed to store {value}')
            failed.append(stats)
        else:
            succeeded.append(value)

    return agg_stats, failed, succeeded


def hash_by_multiplication(value, table, collision_scheme='linear', bucket_size=1):
    """

    :param value: String
    :param table:
    :param collision_scheme:
    :param bucket_size:
    :return:
    """

    try:
        # check for type consistency before we do any other math as math is expensive and cast to int is not
        int_value = int(value)
    except ValueError:
        print("Error converting " + value + " to integer. Discarding then continuing to next value.")
        return

    table_len = len(table)

    # log(n) / log(2) keeps our range limited to n (which will always be 120 but this is more fun)
    m_value = log(table_len) / log_of_2
    ka_value = int_value * a_value
    decimal_value = ka_value - floor(ka_value)

    # from p264 of Cormen
    # h(k) = floor(m(kA mod 1)) but we've done a clever math trick instead of using the mod operator
    key = floor(m_value * decimal_value)

    for i in range(0, bucket_size):
        if table[key][i] == '-1':
            table[key][i] = value
            return format_result(key, value, [], 1)

    if collision_scheme == 'linear':
        return format_result(*probe(key, value, table))

    if collision_scheme == 'quadratic':
        return format_result(*probe(key, value, table, 120, 1, 0.5, 0.5))

    if collision_scheme == 'chain':
        table[key] += [value]
        return format_result(key, value, [], 1)



def hash_by_division(value, table, mod_divisor=120, collision_scheme='linear', bucket_size=1):
    try:
        int_value = int(value)
    except ValueError:
        print("Error converting " + value + " to integer. Discarding then continuing to next value.")
        return

    key = int(floor(int_value % mod_divisor) / bucket_size)

    for i in range(0, bucket_size):
        if table[key][i] == '-1':
            table[key][i] = value
            return format_result(key, value, [], 1)

    if collision_scheme == 'linear':
        return format_result(*probe(key, value, table, mod_divisor, bucket_size))

    if collision_scheme == 'quadratic':
        return format_result(*probe(key, value, table, mod_divisor, bucket_size, 0.5, 0.5))

    if collision_scheme == 'chain':
        table[key] += [int_value]
        return format_result(key, value, [], 1)
