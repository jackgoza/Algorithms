# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.
from math import floor

from lib.collision_handlers import probe


def hash_by_division(value, table, mod_divisor=120, collision_scheme='linear', bucket_size=1):
    try:
        key = int(floor(value % mod_divisor) / bucket_size)
    except ValueError:
        print("Error converting " + value + " to integer. Discarding then continuing to next value.")
        return

    for i in range(0, bucket_size):
        if table[key][i] == '-1':
            table[key][i] = value
            return key, []

    if collision_scheme == 'linear':
        return probe(key, value, table, mod_divisor, bucket_size)

    if collision_scheme == 'quadratic':
        return probe(key, value, table, mod_divisor, bucket_size, 0.5, 0.5)

    if collision_scheme == 'chain':
        table[key] += [value]
        return key, []
