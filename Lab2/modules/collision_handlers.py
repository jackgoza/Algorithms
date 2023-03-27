# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

def check_and_store_item(table, key, value, bucket_size=1):
    if bucket_size == 1:
        if table[key] == '-1':
            table[key] = value

        # If the bucket is size 1 and the value is not '-1', the bucket is full.
        return False

    if bucket_size > 1:
        if table[key] == '-1':
            # If the bucket is size > 1 and init value ('-1'), make the array for the bucket.
            table[key] = [value]

        # If the bucket is size > 1 and the array is already there and
        # len(array) < bucket_size, add the newest value to the bucket.
        elif len(table[key]) < bucket_size:
            table[key] += value


def chain(key, value, table, stack):
    return -1, []


def linear_probe(key, value, table):
    collisions = []
    new_key = key + 1
    while new_key < len(table):
        #    Case 1) The value at the table location for key has not been assigned
        if table[new_key] == '-1':
            table[new_key] = value
            return new_key, collisions

        # If we hit another key, add that key to the list of collisions
        collisions.append(new_key)

        #    Case 2) The table is full and we have traversed the keys following the original
        new_key += 1

    return -1, collisions


def quadratic_probe(original_key, key, value, table, mod_divisor, c1=0.5, c2=0.5, iterations=0, collisions=None):
    if collisions is None:
        collisions = []
    if iterations > 10:
        return -1, collisions

    quad_probe = c1 * (key ** 2) + c2 * key
    new_key = int(quad_probe) % mod_divisor
    if table[new_key] == '-1':
        table[key] = value
        return key, collisions
    else:
        return quadratic_probe(original_key, new_key, value, table, c1, c2, iterations + 1, collisions.append(new_key))
