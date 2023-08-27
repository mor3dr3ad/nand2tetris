"""Parses the given command list."""
import re


class Parser:
    """Parse the file and return the parts of the command for processing."""

    def __init__(self, filename):
        """Initialize the function."""
        with open(filename, 'r', encoding='utf-8') as file:
            self.commands = file.readlines()
            self.cleanCommands = []
            # cleaning logic also works for labels
            for command in self.commands:
                cleanCommand = ''.join(command.split('//')[0].split())
                if cleanCommand != '':
                    self.cleanCommands.append(cleanCommand)
        self.counter = -1
        self.currentCommand = ''

    def resetParser(self):
        """Reset the Parser to start over (first/second pass)."""
        self.counter = -1
        self.currentCommand = ''

    def hasMoreCommands(self):
        """Determine if there more commands in the processed data."""
        return self.counter + 1 < len(self.cleanCommands)

    def advance(self):
        """Move on to the next token.

        does not return anything but makes next command the current
        """
        self.counter += 1
        self.currentCommand = self.cleanCommands[self.counter]

    def commandType(self):
        """Determine the type of command.

        - A_Command for @xxx where xxx is either symbol or decimal
        - B_Command for dest=comp;jump
        - L_Command (actually pseudocommand) for (Xxx) where Xxx is a symbol
        """
        if self.currentCommand == '':
            pass
        if '@' in self.currentCommand:
            return 'A_Command'
        if self.currentCommand[0] == "(":
            return 'L_Command'
        return 'C_Command'

    def symbol(self):
        """Return the symbol 'xxx' or decimal of the current command @xxx.

        only called when command is A_Command or L_Command
        """
        if self.commandType() == 'A_Command':
            return self.currentCommand.split('@')[1]
        elif self.commandType() == 'L_Command':
            return re.search(r'\((.*?)\)', self.currentCommand).group(1)
        return ""

    def dest(self):
        """Return dest mnemoic in the current C-command (8 possibilities).

        Only called with C_Command reminder C_command: dest=comp; jump
        """
        if self.commandType() == 'C_Command':
            if '=' in self.currentCommand:
                return self.currentCommand.split('=')[0]
        return ""

    def comp(self):
        """Return the mnemonic in the current C-command.

        Should be called only with C_Command. C_command: dest=comp; jump
        """
        print(self.currentCommand)
        if self.commandType() == 'C_Command':
            tmp = self.currentCommand
            if '=' in tmp:
                tmp = tmp.split("=")[1]
            return tmp.split(";")[0]
        return ""

    def jump(self):
        """Return the jump mnemoic in the current C-command.

        Should be called only with C_Command
        """
        if self.commandType() == 'C_Command':
            if ';' in self.currentCommand:
                return self.currentCommand.split(";")[1]
        return ""
