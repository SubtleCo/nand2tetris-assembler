""" Functions removing comments and whitespace """


def strip(file: list[str]) -> list:
    """
    Removes comments with the '//' format and non-text characters
    Returns only lines with executable code
    """
    stripped_lines = []
    for line in file:
        line = line.split("//")[0]
        clean_line = line.strip()
        if clean_line:
            stripped_lines.append(clean_line)
    return stripped_lines


def parse(file_name: str) -> list[str]:
    """ Extract data from a file, stripping comments and whitespace """
    with open(file_name, encoding='utf-8') as file:
        executable_code = strip(list(file))
    return executable_code
