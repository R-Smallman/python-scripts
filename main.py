# basic file-sorting script; to sort files by file extension
# utilising built-in functions + python standard libraries

import os # import operating system module
import pathlib # import path module
import shutil # import shutil module



def sorting_function(input_folder, output_folder):
    # search for existing file extensions
    for root, dirs, files in os.walk(input_folder):
        file_extensions = [pathlib.Path(f).suffix for f in files]
        for e in file_extensions:
            e = e.replace(".","")
            if f"{e}-files" not in os.listdir(output_folder):
                os.mkdir(f"{output_folder}/{e}-files")

    # move files , based on file extension , to output folders
    for f in files:
        f_e = pathlib.Path(f).suffix
        shutil.move(f"{input_folder}/{f}", f"{output_folder}/{f_e.replace(".","")}-files/{f}")



def main():
    # definable input + output
    input_folder = "input-files"
    output_folder = "sorted-files"

    # call function
    sorting_function(input_folder, output_folder)


# start programs
main()