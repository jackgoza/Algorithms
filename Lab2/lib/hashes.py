# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

from lib.collision_handlers import chain, probe


def hash_by_division(value, table, mod_divisor=120, collision_scheme='linear', bucket_size=1):
    try:
        key = int(value) % mod_divisor
    except ValueError:
        print("Error converting " + value + " to integer. Discarding then continuing to next value.")
        return

    if table[key][1] == '-1':
        table[key][1] = value
        return key, []

    if collision_scheme == 'linear':
        return probe(key, int(value), table, mod_divisor)

    if collision_scheme == 'quadratic':
        return probe(key, int(value), table, mod_divisor, 0.5, 0.5)

    if collision_scheme == 'chain':
        print('chain')
        return chain(key, value, table)
