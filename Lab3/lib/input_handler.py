# John Goza
# Lab 3 - Dynamic
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
    Reads input from provided filename. Validates that file exists and that file contains at least two valid strings for
    comparison. Strings must be a key:value pair seperated by an = and should not have extra whitespace between lines.
    This function treats extra whitespace / other lines not matching format as ignorable, thus saving us a lot of gross
    error handling

    :param filename: String
    :return: { key1: value1, key2: value2... }
    :throws IOException if file does not exist or is invalid, or if it contains < 2 valid strings
    """
    # check_and_open_file can raise an IOError
    file = check_and_open_file(filename)

    returnable = {}

    for line in file:
        if " = " in line:
            name, value = line.split("=", 1)
            returnable[name.strip()] = value.strip()

    if len(returnable) < 2:
        raise IOError('Input file did not contain enough strings!')

    return returnable
