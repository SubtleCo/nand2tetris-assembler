def export(file_name, binary_instructions):
    export_file_name = file_name.replace('.asm', '.hack')
    with open(export_file_name, 'w') as outgoing:
        for line in binary_instructions:
            outgoing.write(line)
            outgoing.write("\n")
