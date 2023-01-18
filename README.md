# The Hack Assembler

This is project 06 of the [nand2tetris](https://www.nand2tetris.org/project06) course.

Given a set of instructions written in the Hack Assembly Language, this program translates an `.asm` file to a
binary `.hack` file.

## Hack Assembly Contract

- Anything following `//` can be considered a comment and should not be represented in the output machine code
- Whitespace should be ignored
- Lines formatted as `@xxx` are an A_INSTRUCTION
    - If anything other than an integer follows `@`, this is a symbol
    - A_INSRUCTIONS (`@xxx`) exist in binary as:
        - `0vvvvvvvvvvvvvvv` (v v... v 15-bit value of `xxx`)
            - i.e. `@242` = `0000000011110010`
- Lines formatted as `(xxx)` are an L_INSTRUCTION - a symbol/label declaration
- All else are C_INSTRUCTIONS formatted as such:
    - `111accccccdddjjj` where `c` is computation, `d` is destination, and `j` is jump command.
    - values are extracted from the tables below
        - i.e. `D=A` = `1110110000010000`

## Given values

### Symbols

![static_symbols.png](images%2Fstatic_symbols.png)

### Destination and Jump Commands

![dest_jump.png](images%2Fdest_jump.png)

### Computation Commands

![comp.png](images%2Fcomp.png)