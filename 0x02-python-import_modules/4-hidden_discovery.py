#!/usr/bin/python3.8

import marshal

def print_hidden_names(file_path):
    with open(file_path, 'rb') as pyc_file:
        magic = pyc_file.read(4)  # Skip the magic number
        timestamp = pyc_file.read(4)  # Skip the timestamp
        code_object = marshal.load(pyc_file)

        for const in code_object.co_consts:
            if isinstance(const, str) and not const.startswith('__'):
                print(const)

if __name__ == "__main__":
    print_hidden_names('hidden_4.pyc')

