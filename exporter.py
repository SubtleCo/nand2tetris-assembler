def export(file_name: str, binary_instructions: list[str]):
    """ Writes a list of binary instructions to a new file with the .hack suffix """
    export_file_name = file_name.replace('.asm', '.hack')
    with open(export_file_name, 'w') as outgoing:
        for line in binary_instructions:
            outgoing.write(line)
            outgoing.write("\n")
