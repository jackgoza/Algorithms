John Goza

Lab 2 - Hashing

No re-use or reproduction allowed. All rights retained by John Goza.

Source and version history can be found at https://github.com/jackgoza/Algorithms

Written using Intellij IDEA Ultimate 2022.3.2

# Running the program
The program can be run by opening a terminal or command prompt window in the folder containing this code. It must be run
with Python >= 3. The basic command and optional flags are as follows:

```
python Lab2.py
    Runs the program on the input/LabHashingInput.txt file
    and writes the results to the outputs/output.txt file.
    Deletes the output file if already present in specified
    location.
    
Additional flags:
    --input-file 'path/to/file.txt'
                Ingests the file at location passed to flag.
                Locations should be relative to content root
                (e.g. 'inputs/test_input.txt).
                Default: 'inputs/LabHashingInput.txt'

    --output-file 'path/to/file.txt'
                Writes to the file at location passed to flag.
                Locations should be relative to content root
                and any specified sub-directories must exists
                (e.g. 'outputs/test_output.txt')
                Default: 'outputs/output.txt'

    --report
                Writes the metadata from the results into a 
                csv for ease of import into csv editor. Csv
                is saved under 'outputs/report.csv' by default.
    --report-file
                Outputs the report file at location passed to 
                flag. Locations should be relative to content 
                root (e.g. 'outputs/report.csv).
                Default: 'outputs/report.csv'
    --test
                Runs all user-defined test cases in the file
                "inputs/TestHashingInput.txt". Test flag 
                overrides input flag if used together.
```
