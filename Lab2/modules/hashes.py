# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

from collision_handlers import chain, linear_probe, quadratic_probe


def hash_by_division(value, table, mod_divisor=120, collision_scheme='linear', bucket_size=1):
    try:
        key = int(value) % mod_divisor
    except ValueError:
        print("Error converting " + value + " to integer. Discarding then continuing to next value.")
        return

    if table[key] == '-1':
        table[key] = value
        return key, []

    if collision_scheme == 'linear':
        return linear_probe(key, value, table)

    if collision_scheme == 'quadratic':
        return quadratic_probe(key, value, table, mod_divisor)

    if collision_scheme == 'chain':
        return chain(key, value, table)
