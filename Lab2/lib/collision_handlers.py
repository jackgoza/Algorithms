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

def probe(key, value, table, mod, c1=0, c2=0):
    # Store the initial collision
    collisions = [key]

    for i in range(len(table)):
        if c1 != 0 or c2 != 0:
            new_key = int(value + (c1 * (i ** 2)) + (c2 * i)) % mod
        else:
            new_key = int(value + i) % mod
        # If the space is open, take it
        if table[new_key][1] == '-1':
            table[new_key][1] = value
            return new_key, collisions

        # Else (implied due to return statement): if we hit another key, add that key to the list of collisions
        collisions.append(new_key)

    return -1, collisions


def linear_probe(key, value, table):

    # Store the first collision and increment the key
    collisions = [key]
    new_key = key + 1

    # Stop condition is when new_key = key, i.e. when we have visited every table slot
    while new_key != key:
        # If the space is open, take it
        if table[new_key][1] == '-1':
            table[new_key][1] = value
            return new_key, collisions

        # If we hit another key, add that key to the list of collisions
        collisions.append(new_key)

        if new_key >= len(table):
            new_key = 0
        else:
            new_key += 1

    return -1, collisions


def quadratic_probe(original_key, key, value, table, c1=0.5, c2=0.5, collisions=None):
    collisions = [key]
    new_key = key + 1
    if key >= len(table):
        key = 0
    else:
        key += 1
        
    if key == original_key:
        return -1, collisions

    quad_probe = int(c1 * (key ** 2) + c2 * key)

    if table[key][1] == '-1':
        table[key][1] = value
        return key, collisions
    else:
        return quadratic_probe(original_key, key, value, table, c1, c2, collisions + [key])
