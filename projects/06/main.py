"""The main for assembler. calls on parser.

also uses code for support
"""

from parser import Parser
from coder import Code
from symbolHandler import symbolHandler

import os
import sys


class Main:
    """Main class."""

    def main():
        """Run the program."""
        # first check cli args
        if len(sys.argv) > 1:
            filename = os.path.join(os.getcwd(), sys.argv[1])
        else:
            print("Please supply filename")
        # initialize parser
        parser = Parser(filename)

        # initialize symbol class
        symbolhandler = symbolHandler()

        # first pass: run through commands,
        # count value of command and
        # insert into symbol table for each label
        counter = 0
        while parser.hasMoreCommands():
            parser.advance()
            if parser.commandType() == "L_Command":
                # add to symbolTable
                symbolhandler.insertLabel(parser.symbol(), counter)
            else:
                counter += 1
        # need to reset parser somehow,
        parser.resetParser()

        hack_filename = filename.replace('asm', 'hack')
        hack_file = open(hack_filename, 'w')

        code = Code()
        addressCounter = 16
        while parser.hasMoreCommands():
            parser.advance()
            # command = ''
            # A Command can be 3 things:
            # - a number
            # - a known symbol or 
            # - a new symbol
            if parser.commandType() == 'A_Command':
                symbol = parser.symbol()
                if symbol.isdecimal():
                    num = int(symbol)
                elif symbol in symbolhandler.symbolTable:
                    num = symbolhandler.symbolTable[symbol]
                else:
                    num = addressCounter
                    symbolhandler.insertLabel(symbol, addressCounter)
                    addressCounter += 1
                # translate number to binary representation
                hack_file.write(format(num, "016b"))
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
