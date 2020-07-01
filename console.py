#!/usr/bin/python3
""" console.py: Main entry point for the HBNB command interpreter """


import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand - Simple command tests """
    prompt = "(hbnb) "

    # Command methods
    def do_quit(self, line):
        """ do_quit: Quit command """
        return True

    def do_EOF(self, line):
        """ do_EOF: End of File handling """
        print("")  # Print a new line, since EOF doesnt do that on its own
        return True

    def emptyline(self):
        """ emptyline: if an empty line is passed, do nothing """
        pass

    # Help methods
    def help_quit(self):
        """ help_quit: Help documentation for quit """
        print("quit\nQuits the command prompt")

    def help_EOF(self):
        """ help_EOF: Help documentation for EOF """
        print("EOF\nHandles End of File(?)")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
