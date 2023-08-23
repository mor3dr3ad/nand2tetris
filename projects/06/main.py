"""The main for assembler. calls on parser.

also uses code for support
"""

from parser import Parser
from coder import Code

import os
import sys


class Main:
    """Main class."""

    def main():
        """Main function."""
        # first check cli args
        if len(sys.argv) > 1:
            filename = os.path.join(os.getcwd(), sys.argv[1])
        else:
            print("Please supply filename")
        # initialize parser
        parser = Parser(filename)

        hack_filename = filename.replace('asm', 'hack')
        hack_file = open(hack_filename, 'w')

        while parser.hasMoreCommands():
            parser.advance()
            # command = ''
            code = Code()
            if parser.commandType() == 'A_Command':
                # get symbol and translate
                symbol = int(parser.symbol())
                # translate number to binary representation
                hack_file.write(format(symbol, "016b"))
                hack_file.write("\n")
            elif parser.commandType() == 'C_Command':
                # get dest,comp,jump and translate
                dest = code.dest(parser.dest())
                comp = code.comp(parser.comp())
                jump = code.jump(parser.jump())
                # reassemble into binary
                hack_file.write("111" + comp + dest + jump)
                hack_file.write("\n")

            else:
                pass

        hack_file.close()

    if __name__ == "__main__":
        main()
