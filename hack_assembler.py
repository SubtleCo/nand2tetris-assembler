""" Convert an '.asm' file to '.hack binary' with format 'python assembler/hack_assembler.py path/to/file.asm' """

import sys

from file_parser import parse
from symbolizer import symbolize
from encoder import encode
from exporter import export


def main():
    file_name = sys.argv[1]

    executable_code = parse(file_name)

    # first pass - remove and store symbol declarations
    symbolized_code = symbolize(executable_code)

    # second pass - convert to binary
    binary_instructions = encode(symbolized_code)

    export(file_name, binary_instructions)


if __name__ == '__main__':
    main()
