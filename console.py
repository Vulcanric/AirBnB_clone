#!/usr/bin/python3
"""
Contains the entry point of the command interpreter, called
HBNBCommand
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ The backend utility console class used to function as the console """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ Exit the program, similar to the quit function """
        return True

    def do_quit(self, line):
        """
        Exit the program, common to the EOF function
        SYNOPSIS: quit
        """
        return True

    def emptyline(self):
        """
        Overwrite the emptyline function to do nothing when an empty
        line is passed in response to the prompt
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
