# John Goza
# Lab 1 - Strassen's algorithm
# No re-use or reproduction allowed. All rights retained by John Goza.

# This file is not for evaluation in Lab1. It is included SOLELY as a convenience for the programmer to make
# more test cases. It is not referenced in any other file and should NOT be considered for grading purposes
# (it's really gross)

def make_matrix(n):
    with open("large_matrix.txt", 'w') as file:
        file.write(f"{n}\n")
        for i in range(0, n):
            for j in range(0, n):

                if i == j:
                    file.write("1 ")
                else:
                    file.write("0 ")
            file.write("\n")
        file.write("\n")
        for i in range(0, n):
            for j in range(0, n):

                if i == j:
                    file.write("1 ")
                else:
                    file.write("0 ")
            file.write("\n")
        file.write("\n")

make_matrix(1024)