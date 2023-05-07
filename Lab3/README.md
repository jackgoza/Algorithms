John Goza

Lab 3 - Dynamic

No re-use or reproduction allowed. All rights retained by John Goza.

Source and version history can be found at https://github.com/jackgoza/Algorithms

Written using Intellij IDEA Ultimate 2022.3.2

# Running the program
The program can be run by opening a terminal or command prompt window in the folder containing this code. It must be run
with Python >= 3. The basic command and optional flags are as follows:

```
python Lab3.py
    Runs the program on the input/DynamicLabInput.txt file
    and writes the results to the outputs/output.txt file.
    Deletes the output file if already present in specified
    location.
    
Additional flags:
    --console
                Logs output to the console as well as an output file.

    --input-file 'path/to/file.txt'
                Ingests the file at location passed to flag.
                Locations should be relative to content root
                (e.g. 'inputs/test_input.txt).
                Default: 'inputs/TestInput.txt'

    --output-file 'path/to/file.txt'
                Writes to the file at location passed to flag.
                Locations should be relative to content root
                and any specified sub-directories must exists
                (e.g. 'outputs/test_output.txt')
                Default: 'outputs/output.txt'

    --quiet
                Prevents output of cost matricies
                
    --test
                Runs all user-defined test cases in the file
                "inputs/TestInput.txt". Test flag is overwritten
                by input flag if used together.
```
