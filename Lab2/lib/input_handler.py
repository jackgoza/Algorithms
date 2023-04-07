# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

from os import path


def check_and_open_file(filename):
    if not path.exists(filename):
        raise IOError("Provided filename does not exist")

    if not path.isfile(filename):
        raise IOError("Provided filename points to a directory")

    return open(filename, "r")


def parse_file(filename):
    # check_and_open_file can raise an IOError
    file = check_and_open_file(filename)

    lists_to_hash = []
    curr_list = []

    for line in file:
        curr_line = line.strip()

        if curr_line.isdigit():
            curr_list.append(curr_line)
        elif (curr_line == '' or curr_line.isspace()) and curr_list != []:
            lists_to_hash.append(curr_list)
            curr_list = []
        elif curr_line == '' or curr_line.isspace():
            continue
        else:
            print(f"Skipping invalid line: {line}")

    lists_to_hash.append(curr_list)
    file.close()
    
    if len(list(filter(None, lists_to_hash))) == 0:
        raise IOError("No valid input found in file!")
    
    return lists_to_hash


def ingest_file(filename):
    return parse_file(filename)
