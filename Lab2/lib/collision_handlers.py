# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.
from math import floor


def probe(key, value, table, mod=120, bucket_size=1, c1=0, c2=0):
    # todo: add bucket logic
    # Store the initial collision
    collisions = [key]
    # we have already made one comparison which is how we ended up here
    comparisons = 1

    # This has already been checked so no need to handle type error here
    int_value = int(value)

    for i in range(int(len(table) / bucket_size)):

        # CASE: quadratic probing
        if c1 != 0 or c2 != 0:
            new_key = int(floor((int(int_value + (c1 * (i ** 2)) + (c2 * i)) % mod) / bucket_size))

        # CASE: linear probing
        else:
            new_key = int(floor((int(int_value + i) % mod) / bucket_size))

        # If: the space is open, take it
        for j in range(0, bucket_size):
            try:
                # we are about to make a comparison
                comparisons += 1
                if table[new_key][j] == '-1':
                    table[new_key][j] = value
                    return new_key, value, collisions, comparisons
            except Exception as e:
                return e

        # Else: (implied due to return statement): if we hit another key, add that key to the list of collisions
        collisions.append(new_key)

    return -1, value, collisions, comparisons
