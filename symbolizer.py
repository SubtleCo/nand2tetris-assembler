""" Strip symbol declarations from executable code and store in symbol table """

from symbols import symbols


def symbolize(code):
    line_number = 0
    symbolized_code = []
    for line in code:
        if "(" in line:
            name = line[1:-1]
            symbols[name] = line_number
        else:
            symbolized_code.append(line)
            line_number += 1
    return symbolized_code
