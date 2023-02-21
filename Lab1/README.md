John Goza


Lab 1 - Strassen's algorithm


No re-use or reproduction allowed. All rights retained by John Goza.

Source and version history can be found at https://github.com/jackgoza/Algorithms

# Running the program
The program can be run by opening a terminal or command prompt window in the folder containing this code. It must be run
with Python >= 3. The basic command and optional flags are as follows:

```
python Lab1.py
    Runs the program on the input/LabStrassenInput.txt file
    and places the output in output.txt in the content root.
    Appends to output file if already present in content
    root. Does not output the resulting multiplied matrices;
    only the input and the complexity measurements.
    
Additional flags:
    --input 'path/to/file.txt'
                Ingests the file at location passed to flag.
                Locations should be relative to content root
                (e.g. 'inputs/test_input.txt).
                Default: 'input/LabStrassenInput.txt'
    --output 'path/to/file.txt'
                Writes to the file at location passed to flag.
                Locations should be relative to content root
                and any specified sub-directories must exists
                (e.g. 'output/test_output.txt' if and only if
                        you make a folder called 'output' in
                        the content root)
                Default: 'output.txt'
    --resultants
                Writes the resulting matrices from both forms
                of matrix multiplication. Useful to validate 
                that multiplication functions correctly and
                outputs a correct result.
    --clean
                Deletes existing output if found. Helpful for
                running program repeatedly.
    --test
                Runs all user-defined test cases in the file
                "inputs/test_input.txt". Test flag overrides
                input flag if used together.
```
