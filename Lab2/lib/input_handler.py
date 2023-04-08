# John Goza
# Lab 2 - Hashing
# No re-use or reproduction allowed. All rights retained by John Goza.

from os import path


def check_and_open_file(filename):
    """
    Opens file for reading if it exists, is not a directory, and is readable
    :param filename: String
    :return: FileStream
    :throws IOError if specified file does not exist, is a directory, or is not readable
    """
    if not path.exists(filename):
        raise IOError("Provided filename does not exist.")

    if not path.isfile(filename):
        raise IOError("Provided filename points to a directory.")

    opened = open(filename, "r")

    if not opened.readable():
        opened.close()
        raise IOError("File is read-locked. Are your permissions correct?")

    return opened


def parse_file(filename):
    """
    Reads input from provided filename. Validates that file exists and that file contains at least one block of
    hashable values. Blocks must be one integer value per line and may not have extra whitespace between lines.
    Extra whitespace is interpreted as "end of block". Lines with non-digit characters are ignored.
    :param filename: String
    :return: Array[ Array[ String ] ]
    :throws IOException if file does not exist or is invalid, or if it contains no valid blocks
    """
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
