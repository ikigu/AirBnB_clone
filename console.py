#!/usr/bin/python3
"""Defines the HBNBCommand class for command line interpretation."""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    intro = "Welcome to the hbnb command interpreter type 'help' to list available commands"

    def do_quit(self, arg):
        """Quit the command interpreter."""
        print("Bye!")
        exit()

    def emptyline(self):
        """Handle an empty line input."""
        pass

    def do_help(self, arg):
        """Show help for available commands."""
        print("Documented commands (type help <topic> for more info):")
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

