""" Functions handling the conversion of assembly commands to binary """
from itertools import count

from constants.comp_table import comp_table
from constants.dest_table import dest_table
from constants.jump_table import jump_table
from constants.op_codes import A_OP_CODE, C_OP_CODE
from symbols import symbols


variable_location = count(16)

def format_C_instruction(comp: str, dest: str, jump: str) -> str:
    """ Translate elements of C instruction to binary, format command"""
    bin_comp = comp_table.get(comp)
    bin_dest = dest_table.get(dest)
    bin_jump = jump_table.get(jump)
    return C_OP_CODE + bin_comp + bin_dest + bin_jump


def format_A_instruction(line: str):
    """ Translate elements of A instruction to binary, format command"""
    address = line.split('@')[1]
    try:
        # Indicates a standard integer address
        parsed_address = int(address)
    except ValueError:
        # Indicates a symbol
        parsed_address = symbols.get(address)
        if parsed_address is None:
            # Indicates a variable - needs to be set in symbol table
            symbols[address] = next(variable_location)
            parsed_address = symbols[address]
    bin_address = "{:015b}".format(parsed_address)
    return A_OP_CODE + bin_address


def encode(executable_code: list) -> list:
    """ Translates a list of executable assembly commands to binary """
    instructions = []
    for i, line in enumerate(executable_code):
        if "@" in line:
            # A instruction
            formatted_address = format_A_instruction(line)
            instructions.append(formatted_address)
        elif "=" in line and ";" in line:
            # C instruction with COMP, DEST, JUMP
            dest, comp_jump = line.split("=")
            comp, jump = comp_jump.split(";")

            binary = format_C_instruction(comp, dest, jump)
            instructions.append(binary)

        elif "=" in line:
            # C instruction with COMP, DEST
            dest, comp = line.split("=")
            jump = "null"
            binary = format_C_instruction(comp, dest, jump)
            instructions.append(binary)

        elif ";" in line:
            # C instruction with COMP, JUMP
            comp, jump = line.split(";")
            dest = "null"
            binary = format_C_instruction(comp, dest, jump)
            instructions.append(binary)
        else:
            raise ValueError({"message": f"You've got an error with the line {line}"})

    return instructions


