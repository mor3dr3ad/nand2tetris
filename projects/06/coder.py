"""
a class/program that takes as input some code in assembly language
and translates to machine code.
we do not need to worry how fields were obtained, only need to translate.
distinguish between A/C/
"""

class Code:
    """
    class that takes as input a mnemonic and
    translates it into binary
    """
    def __init__(self):
        """instantiates the class"""

        self.dest_dict = {
            "": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111"
        }

        self.jump_dict = {
            "": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }

        self.comp_dict = {
            "0": "101010",
            "1": "111111",
            "-1": "111010",
            "D": "001100",
            "A": "110000",
            "M": "110000",
            "!D": "001101",
            "!A": "110001",
            "!M": "110001",
            "-D": "001111",
            "-A": "110011",
            "-M": "110011",
            "D+1": "011111",
            "A+1": "110111",
            "M+1": "110111",
            "D-1": "001110",
            "A-1": "110010",
            "M-1": "110010",
            "D+A": "000010",
            "D+M": "000010",
            "D-A": "010011",
            "D-M": "010011",
            "A-D": "000111",
            "M-D": "000111",
            "D&A": "000000",
            "D&M": "000000",
            "D|A": "010101",
            "D|M": "010101"
        }

    def comp(self, command):
        """translates comp
           switches on 'a' bit (when a=1)"""
        return self.comp_dict[command]

    def dest(self, command):
        """translates dest """
        return self.dest_dict[command]

    def jump(self, command):
        """translates jump"""
        return self.jump_dict[command]
